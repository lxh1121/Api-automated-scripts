# coding=utf-8;
"""
Created on 2022/3/7 5:58 下午
Author: lxh
Project: 
"""
from setuptools import setup, find_packages

install_requires = []
tests_requires = []

with open('requirements.txt') as f:
    for r in f:
        install_requires.append(r)

setup(
    name='quality-api-trade-job',
    long_description=open('README.md').read(),
    author="qa",
    author_email="qa@caibeike.com",
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    url="",
    tests_require=tests_requires,
    install_requires=install_requires,
)
