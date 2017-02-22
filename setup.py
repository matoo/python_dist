#!/usr/bin/env python3

from distutils.core import setup
from distutils.command.bdist_dumb import bdist_dumb
from setuptools import find_packages

class custom_bdist_dumb(bdist_dumb):

    def reinitialize_command(self, name, **kw):
        cmd = bdist_dumb.reinitialize_command(self, name, **kw)
        if name == 'install':
            cmd.install_lib = '/'
        return cmd


setup(
  cmdclass = {'bdist_dumb': custom_bdist_dumb},
  name='deploy',
  py_modules = ['__main__', 'decorator', 'mail'],
  packages=find_packages(),
)
