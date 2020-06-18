from setuptools import setup, find_packages

setup(
  name = 'pysdf',
  version = '1.0',
  description = 'Sdf to urdf converter',
  author = 'me',
  author_email = 'myemail@mail',
  packages = find_packages(include=['pysdf', 'pysdf.*', 'pysdf/bin/*']),
  scripts = ['pysdf/bin/sdf2urdf.py']
)
