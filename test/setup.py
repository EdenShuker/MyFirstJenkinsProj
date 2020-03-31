from setuptools import setup, find_packages

setup(
    name='jenkins_proj_test',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['pytest', 'jenkins_proj']
)
