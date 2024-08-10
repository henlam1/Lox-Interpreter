from setuptools import setup, find_packages

setup(
    name='lox',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
        ]
    }
)