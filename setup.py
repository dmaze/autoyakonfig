from __future__ import absolute_import
from setuptools import setup, find_packages
setup(name='autoyakonfig',
      version='0.1',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'autoyakonfig = autoyakonfig.main:main',
          ],
      }
  )
