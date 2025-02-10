from . import library as ae

T_C_IN = 27.0                                                             # JIS測定時の室内温度 [℃]
T_C_EX = 35.0                                                             # JIS測定時の室外温度 [℃]
X_C_IN = ae.absolute_humidity_from_e(ae.vapor_pressure_wet_bulb(19, 27))  # JIS測定時の室内絶対湿度 [kg/kg']  湿球温度は19℃
X_C_EX = ae.absolute_humidity_from_e(ae.vapor_pressure_wet_bulb(24, 35))  # JIS測定時の室外絶対湿度 [kg/kg']  湿球温度は24℃

T_H_IN = 20.0                                                             # JIS測定時の室内温度 [℃]
T_H_EX =  7.0                                                             # JIS測定時の室外温度 [℃]
X_H_IN = ae.absolute_humidity_from_e(ae.vapor_pressure_wet_bulb(15, 20))  # JIS測定時の室内絶対湿度 [kg/kg']  湿球温度は15℃（最高温度）
X_H_EX = ae.absolute_humidity_from_e(ae.vapor_pressure_wet_bulb( 6,  7))  # JIS測定時の室外絶対湿度 [kg/kg']  湿球温度は6℃
