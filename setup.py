import argparse
import os
import subprocess
import sys

from setuptools import setup, Extension, Command, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install
from distutils.errors import DistutilsArgError

this_dir = os.path.realpath(os.path.dirname(__file__))


def main():
    setup(
        name='postal',
        version='0.3',
        install_requires=[
            'six',
        ],
        setup_requires=[
            'nose>=1.0'
        ],
        ext_modules=[
            Extension('postal._expand',
                      sources=['postal/pyexpand.c'],
                      libraries=['postal'],
                      include_dirs=['/usr/local/include'],
                      library_dirs=['/usr/local/lib'],
                      extra_compile_args=['-std=c99',
                                          '-Wno-unused-function'],
                      ),
            Extension('postal._parser',
                      sources=['postal/pyparser.c'],
                      libraries=['postal'],
                      include_dirs=['/usr/local/include'],
                      library_dirs=['/usr/local/lib'],
                      extra_compile_args=['-std=c99',
                                          '-Wno-unused-function'],
                      ),
        ],
        packages=find_packages(),
        zip_safe=False,
        url='https://github.com/openvenues/pypostal',
        description='Python bindings to libpostal for fast international address parsing/normalization',
        license='MIT License',
        maintainer='mapzen.com',
        maintainer_email='pelias@mapzen.com',
        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: C',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Topic :: Text Processing :: Linguistic',
            'Topic :: Scientific/Engineering :: GIS',
            'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    )


if __name__ == '__main__':
    main()
