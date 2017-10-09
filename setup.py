from setuptools import setup
setup(
  name = 'rtapi2',
  packages = ['rtapi2'],
  version = '0.1',
  description = 'Wrapper for RT REST API Version 2',
  author = 'Jacob Rickerd',
  author_email = 'jacobrickerd@gmail.com',
  license='MIT',
  url = 'https://github.com/Rickerd0613/rtapi2',
  download_url = 'https://github.com/Rickerd0613/rtapi2/archive/0.1.tar.gz',
  keywords = ['request', 'tracker', 'rt', 'api'],
  install_requires=[
	'requests',
  ],
)
