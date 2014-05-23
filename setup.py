from setuptools import setup
import os


def read(*parts):
    retval = ''
    with open(os.path.join(*parts), 'r') as f:
        retval = f.read()

    return retval


def requirements():
    return read('requirements.txt').split()


setup(
    name='yggdrasil',
    url='https://github.com/Moguri/yggdrasil',
    license='Apache Software License',
    install_requires=requirements(),
)
