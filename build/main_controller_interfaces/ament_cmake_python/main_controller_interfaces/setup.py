from setuptools import find_packages
from setuptools import setup

setup(
    name='main_controller_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('main_controller_interfaces', 'main_controller_interfaces.*')),
)
