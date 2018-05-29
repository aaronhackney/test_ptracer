from setuptools import setup

setup(name='test_ptracer',
      version='0.1',
      description='This is an example how the ASDM interface can allow us to programatically run packet-tracer tests',
      url='http://github.com/aaronhackney/test_ptrace',
      author='Aaron Hackney',
      author_email='ahack210@gmail.com',
      license='MIT',
      packages=['test_ptracer'],
      install_requires=[
          'bs4',
          'beautifulsoup4',
          'colorama',
      ],
      scripts=['bin/test_ptracer.py'],
      zip_safe=False)
