from setuptools import setup, find_packages

setup(
    name="archenv",  # パッケージ名
    version="0.1.0",  # バージョン
    packages=find_packages(include=["archenv", "archenv.*"]),  # 明示的に archenv を含める
    install_requires=[
        "requests",
        "numpy",
        "pandas"  # 必要なら追加
    ],
    include_package_data=True,
    zip_safe=False,
)
