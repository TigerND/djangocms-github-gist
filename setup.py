#!/usr/bin/env python

from setuptools import setup

setup(
    name='djangocms-github-gist',
    version='0.1.1',
    description='A GuitHub Gist plugin for Django CMS',
    author='Aleksandr Zykov',
    author_email='tiger@vilijavis.lt',
    url='https://github.com/TigerND/djangocms-github-gist',
    packages=[
        'djangocms_githubgist',
        'djangocms_githubgist.migrations',
    ],
    data_files=[
    ],
    install_requires = [
        'django-cms>=3.2.5',
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
