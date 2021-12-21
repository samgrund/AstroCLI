from setuptools import setup, find_packages


setup(
    name='astrocli',
    version='0.1',
    license='MIT',
    author="Samuel Grund",
    author_email='samuel_grund@hotmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/samgrund/astrocli,
    keywords='pystrometry',
    install_requires=[
          'astropy',
      ],

)