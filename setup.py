from setuptools import setup, find_packages

setup(
    name="archenv",
    version="0.1.0",
    packages=find_packages(include=["archenv", "archenv.*"]),
    install_requires=[
        "requests",
        "numpy",
        "pandas"
    ],
    include_package_data=True,
)
