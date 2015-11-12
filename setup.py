from setuptools import setup, find_packages

with open('README.rst') as f:
    longdesc = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')


setup(
    name='numpile',
    version='0.0.0',
    author='Stephen Diehl',
    author_email='blaze-dev@continuum.io',
    description='Numeric specializer for Python code',
    long_description=longdesc,
    install_requires=install_requires,
    packages=find_packages()
)
