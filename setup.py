# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pyyyc_tictactoe',
    version='0.0.0',
    description='PyYYC collaborative tic-tac-toe learning project',
    long_description=open('README.rst', 'r').read(),
    keywords=['python'],
    install_requires=[
        'pytest',
        'flake8',
        'coverage',
        'cuvner',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    author='PyYYC',
    author_email='organizers@pyyyc.org',
    url='https://www.meetup.com/py-yyc/',
    license='MIT',
    packages=[
        'ttt',
    ],
)
