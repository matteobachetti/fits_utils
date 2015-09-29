#!/usr/bin/env python

from setuptools import setup

setup(name='Fits Utils',
      version='0.1',
      description='Fits manipulation Utilities',
      author='Matteo Bachetti',
      author_email='matteo@matteobachetti.it',
      url='www.matteobachetti.it',
      packages=['fits_utils'],
      entry_points={
        'console_scripts': ['copy-spectra=fits_utils.copy_spectra:main']}
      )
