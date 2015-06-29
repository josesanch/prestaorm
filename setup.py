# encoding: utf-8
from distutils.core import setup

from setuptools import find_packages

import prestaorm

setup(
    name='prestaorm',
    version=prestaorm.VERSION,
    author='José Sánchez Moreno',
    author_email='jose@o2w.es',
    packages=find_packages(),
    #    test_suite="tests",
    license='MIT',
    description=u'Access to prestashop API using django similar ORM Syntax',
    long_description=open('README.rst').read(),
    url='https://github.com/josesanch/prestaorm',
    platforms="All platforms",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],

)
