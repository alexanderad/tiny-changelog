# Tiny Changelog

Yet another approach to generate simple and slim CHANGELOG file.

## Install

    pip install tiny-changelog

## Usage

    usage: tiny-changelog [-h] [-t TOKEN] -p PROJECT [-s START_DATE] [-o OUTPUT]
                          [--with-unreleased]

    Generate CHANGELOG file.

    optional arguments:
      -h, --help            show this help message and exit
      -t TOKEN, --token TOKEN
                            Github token
      -p PROJECT, --project PROJECT
                            Github project (<owner>/<repo>)
      -s START_DATE, --start-date START_DATE
                            List entries starting as early as YYYY-MM-DD
      -o OUTPUT, --output OUTPUT
                            Output file, defaults to CHANGELOG.md
      --with-unreleased     Include unreleased merged pull requests
