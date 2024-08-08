from setuptools import setup

setup(
    name='docxtplevm',
    version='0.1',
    description='A quick and dirty solution for vertical cell merge in docxtpl',
    author='Peter Lei',
    license='LGPL 2.1',
    packages=['docxtplevm'],
    install_requires=[
        'docxtpl'
    ],
    zip_safe=False)
