#! /usr/bin/env python
import os
from setuptools import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules']

setup(
    name='django-prices-vatlayer',
    author='Mirumee Software',
    author_email='hello@mirumee.com',
    description='vatlayer.com support for django',
    license='BSD',
    version='1.0.0b1',
    url='https://github.com/mirumee/django-prices-vatlayer',
    packages=[
        'django_prices_vatlayer',
        'django_prices_vatlayer.migrations',
        'django_prices_vatlayer.management',
        'django_prices_vatlayer.management.commands'],
    include_package_data=True,
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.11', 'requests', 'dj-database-url', 'prices>=1.0.0',
        'pytest-django', 'jsonfield'],
    platforms=['any'],
    test_suite='django_prices_vatlayer.tests',
    tests_require=['pytest'],
    zip_safe=False)
