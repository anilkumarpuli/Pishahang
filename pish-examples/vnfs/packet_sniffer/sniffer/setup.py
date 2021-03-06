from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# configure plugin name here
CONTAINER_NAME = "rtmp-sniffer"

# generate a name without dashes
CONTAINER_NAME_CLEAR = "rtmp_sniffer"

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=CONTAINER_NAME_CLEAR,

    version='1.0',

    description='RTMP packet sniffer',
    long_description=long_description,

    # The project's main homepage.
    url='http://github.com/CN-UPB/Pishahang',

    # Author details
    author='Hadi Razzaghi Kouchaksaraei',
    author_email='hadi.razzaghi@upb.de',

    # license
    license='Apache 2.0',

    packages=find_packages(),
    install_requires=['mongoengine', 'amqpstorm', 'PyYAML'],
    setup_requires=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            '%s=%s.__main__:main' % (CONTAINER_NAME, CONTAINER_NAME_CLEAR),
        ],
    },
)
