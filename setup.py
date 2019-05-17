from setuptools import setup, find_packages


setup(name='cli-app',
      version='0.1',
      description='The cli-app in the world',
      author='Square Huang',
      author_email='',
      license='MIT',
      packages=find_packages(),
      scripts=['bin/mock_service'],
      entry_points={
          'console_scripts': ['cli_app=cli_app.cli:base_cli']
      },
      zip_safe=False)
