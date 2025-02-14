from setuptools import setup, find_packages

setup(
    name="ac_model",
    version="0.1.0",
    packages=find_packages(include=["ac_model", "ac_model.*"]),
    install_requires=[
        "requests",
        "numpy",
        "pandas",
        "archenv",  # ここではパッケージ名のみ
    ],
    dependency_links=[
        "git+https://github.com/iguchi-lab/archenv.git#egg=archenv",
    ],
    include_package_data=True,
)
