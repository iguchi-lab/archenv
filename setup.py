from setuptools import setup, find_packages

setup(
    name="archenv",  # 自分のパッケージ名
    version="0.1.0",  # バージョン番号
    packages=find_packages(),  # パッケージを自動検出
    install_requires=[
        "requests",  # 依存関係のライブラリ
        "numpy",
    ],
    dependency_links=[
    ],
    include_package_data=True,
    zip_safe=False,
)
