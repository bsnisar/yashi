from setuptools import setup, find_packages

setup(
    name='shai',
    version='0.0.1',
    author = 'Bohdan Snisar',
    author_email = 'bogdan.sns@gmail.com',
    url='https://github.com/bsnisar/shai', 
    description='Just ask what shell should to for you',
    packages=find_packages(exclude=['tests']), 
    entry_points={
        'console_scripts': [
            'shai=shai.cli',
        ],
    },
    install_requires=[
        'rich',
        'cohere',
    ],
)
