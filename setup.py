from setuptools import setup, find_packages

setup(
    name='shai',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'shai=shai.cli:calculate',
        ],
    },
)
