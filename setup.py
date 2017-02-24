# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

from katana import __version__


setup(
    name='katana-sdk-python2',
    version=__version__,
    url='http://kusanagi.io/',
    license='MIT',
    author='Jerónimo Albi',
    author_email='jeronimo.albi@kusanagi.io',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'gevent==1.2.1',
        'click==6.4',
        'pyzmq==15.4.0',
        'msgpack-python==0.4.7',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
)
