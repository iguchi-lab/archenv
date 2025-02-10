import numpy as np
import archenv.const as const

# 空気密度 [kg/m³]
def air_density(temp_c):
    """
    温度 [℃] における空気の密度を計算する。
    :param temp_c: 温度 [℃]
    :return: 密度 [kg/m³]
    """
    return const.STANDARD_ATMOSPHERIC_PRESSURE / (const.GAS_CONSTANT_DRY_AIR * absolute_temperature(temp_c))

# 空気の熱容量 [J/K]
def air_heat_capacity(volume_m3, temp_c):
    """
    容積 [m³] の空気の熱容量を計算する。
    :param volume_m3: 空気の容積 [m³]
    :param temp_c: 温度 [℃]
    :return: 熱容量 [J/K]
    """
    return volume_m3 * const.SPECIFIC_HEAT_AIR * air_density(temp_c) * 1000

# 湿り空気の比熱 [J/K]
def air_specific_heat(x):
    """
    重量絶対湿度[kg/kg(DA)]の湿り空気の比熱を計算する。
    :param x: 重量絶対湿度 [kg/kg(DA])
    :return: 湿り空気の比熱 [kJ/kg]
    """
    return const.SPECIFIC_HEAT_AIR + const.SPECIFIC_HEAT_WATER_VAPOR * x 

# 絶対温度 [K]
def absolute_temperature(temp_c):
    """
    摂氏温度 [℃] を絶対温度 [K] に変換する。
    :param temp_c: 温度 [℃]
    :return: 絶対温度 [K]
    """
    return temp_c + const.KELVIN_OFFSET

# 飽和水蒸気圧計算用の補助関数
def T_dash(temp_c):
    return absolute_temperature(100.0) / absolute_temperature(temp_c)

# エネルギー単位変換
def wh_to_mj(value):
    """
    エネルギー単位変換: Wh から MJ への変換。
    :param value: エネルギー [Wh]
    :return: エネルギー [MJ]
    """
    return value * 3.6 / 1000

def mj_to_wh(value):
    """
    エネルギー単位変換: MJ から Wh への変換。
    :param value: エネルギー [MJ]
    :return: エネルギー [Wh]
    """
    return value * 1000 / 3.6

# 飽和水蒸気圧 [Pa]
def saturation_vapor_pressure(temp_c):
    """
    温度 [℃] における飽和水蒸気圧を計算する。
    :param temp_c: 温度 [℃]
    :return: 飽和水蒸気圧 [Pa]
    """
    t_dash = T_dash(temp_c)
    log_ps = (
        -7.90298 * (t_dash - 1)
        + 5.02808 * np.log10(t_dash)
        - 1.3816e-7 * (np.power(10, 11.344 * (1 - 1 / t_dash)) - 1)
        + 8.1328e-3 * (np.power(10, -3.4919 * (t_dash - 1)) - 1)
        + np.log10(const.STANDARD_ATMOSPHERIC_PRESSURE / 100)
    )
    return np.power(10, log_ps) * 100

# 水蒸気圧 [Pa]
def vapor_pressure(temp_c, humidity):
    """
    温度 [℃] と相対湿度 [%] から水蒸気圧を計算する。
    :param temp_c: 温度 [℃]
    :param humidity: 相対湿度 [%]
    :return: 水蒸気圧 [Pa]
    """
    return humidity / 100 * saturation_vapor_pressure(temp_c)

#湿球温度を用いた蒸気圧 e_w を計算
def vapor_pressure_wet_bulb(T_w, T_d, P=const.STANDARD_ATMOSPHERIC_PRESSURE):
    A = 0.00066  # 湿球係数 (hPa/Pa)
    e_s_Tw = saturation_vapor_pressure(T_w)
    e_w = e_s_Tw - A * P * (T_d - T_w)
    return e_w

# 絶対湿度 [kg/kg]
def absolute_humidity_from_e(e):
    """
    水蒸気分圧[Pa]から重量絶対湿度[kg/kg(DA)]を計算する。
    :param e: 水蒸気分圧[Pa]
    :return: 重量絶対湿度[kg/kg(DA)]
    """
    return 0.622 * (e / (const.STANDARD_ATMOSPHERIC_PRESSURE - e))

# 絶対湿度 [kg/kg]
def absolute_humidity(temp_c, humidity):
    """
    温度 [℃] と相対湿度 [%] から絶対湿度を計算する。
    :param temp_c: 温度 [℃]
    :param humidity: 相対湿度 [%]
    :return: 絶対湿度 [kg/kg]
    """
    e = vapor_pressure(temp_c, humidity)
    return absolute_humidity_from_e(e)

# エンタルピ計算
def sensible_enthalpy(temp_c):
    """
    顕熱エンタルピ [kJ/kg] を計算する。
    :param temp_c: 温度 [℃]
    :return: 顕熱エンタルピ [kJ/kg(DA)]
    """
    return const.SPECIFIC_HEAT_AIR * temp_c

def latent_enthalpy(temp_c, humidity=None, x=None):
    """
    潜熱エンタルピ [kJ/kg] を計算する。
    :param temp_c: 温度 [℃]
    :param humidity: 相対湿度 [%]
    :return: 潜熱エンタルピ [kJ/kg(DA)]
    """
    if humidity is not None:
        return absolute_humidity(temp_c, humidity) * (const.LATENT_HEAT_VAPORIZATION + const.SPECIFIC_HEAT_WATER_VAPOR * temp_c)
    elif x is not None:
        return x * (const.LATENT_HEAT_VAPORIZATION + const.SPECIFIC_HEAT_WATER_VAPOR * temp_c)

def total_enthalpy(temp_c, humidity=None, x=None):
    """
    全熱エンタルピ [kJ/kg] を計算する。
    :param temp_c: 温度 [℃]
    :param humidity: 相対湿度 [%]
    :return: 全熱エンタルピ [kJ/kg(DA)]
    """
    if humidity is not None:
        return sensible_enthalpy(temp_c) + latent_enthalpy(temp_c, humidity=humidity)
    elif x is not None:
        return sensible_enthalpy(temp_c) + latent_enthalpy(temp_c, x=x)
