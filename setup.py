# setup.py
from setuptools import setup, find_packages

setup(
    name='rune-ai',
    version='0.1',
    description='A music generation AI',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rune-ai = rune_ai.main:main',
        ],
    },
)