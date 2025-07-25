from setuptools import setup, find_packages

setup(
    name="dobot_api",
    version="3.0.0",
    description="Dobot Robot API for TCP/IP communication",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
    ],
    python_requires=">=3.6",
)
