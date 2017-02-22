# Create setup.py file in packages root directory
cat <<EOS > package_dir/setup.py
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
  name='deploy',  # package name
  py_modules = ['__main__', 'decorator', 'mail'],  # module name which is in root directory
  packages=find_packages(),
)
EOS

# Build Distributions
python3 setup.py bdist --format=zip
echo '#!/usr/bin/env python3' | cat -  dist/package_name > where_to_install/app_name
chmod u+x where_to_install/app_name
