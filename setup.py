# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bcpp-clinic-labs',
    version='0.1.1',
    author=u'Coulson Thabo Kgathi',
    author_email='ckgathi@gmail..com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/botswana-harvard/bcpp-clinic-labs',
    license='GPL license, see LICENSE',
    description='lab profiles for bcpp-clinic-subject',
    long_description=README,
    zip_safe=False,
    keywords='lab profiles edc bcpp-clinic-subject',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
