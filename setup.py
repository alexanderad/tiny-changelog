#!/usr/bin/env python
import re

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

version_regex = re.compile("VERSION\s*=\s*'(.*?)'$")
with open('changelog/__init__.py') as stream:
    VERSION = version_regex.search(stream.read()).group(1)


setup(
    name='tiny-changelog',
    version=VERSION,
    description='Tiny Changelog Generator',
    long_description=readme,
    url='https://github.com/alexanderad/tiny-changelog',
    license='MIT',
    author='Alexander Shchapov',
    author_email='alexander.shchapov@gmail.com',
    install_requires=['sortedcontainers'],
    packages=find_packages(),
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tiny-changelog=changelog.changelog:main'
        ]
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ),
)

