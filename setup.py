# laraflask/setup.py

from setuptools import setup, find_packages

setup(
    name='laraflask',
    version='0.1',
    packages=find_packages(),
    # Include any other metadata you want
    author='Teguh Rijanandi',
    author_email='teguhrijanandi02@gmail.com',
    description='A flask package for Laraflask',
    license='MIT',
    keywords='laraflask flask package',
    url='https://github.com/laraflask/laraflask',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)

# Build the Distribution Package:
# $ python setup.py sdist

# Install the Distribution Package:
# $ pip install dist/laraflask-0.1.tar.gz

# Uninstall the Distribution Package:
# $ pip uninstall laraflask