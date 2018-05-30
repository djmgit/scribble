# setup.py

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='scribble',
      version='0.1',
      description='Terminal based application to take notes',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='cli terminal script',
      url='https://github.com/djmgit/scribble',
      author='Deepjyoti Mondal',
      author_email='djmdeveloper060796@gmail.com',
      license='MIT',
      packages=['scribble_cli'],
      install_requires=[
          'requests',
          'tabulate',
          'python-editor'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['scribble=scribble_cli.scribble:main'],
      },
      include_package_data=True,
      zip_safe=False)
