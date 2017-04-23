# Tiny Changelog

Yet another approach to generate simple and slim CHANGELOG file.

## Install

    pip install tiny-changelog

## Usage

    $ tiny-changelog -h
    usage: tiny-changelog [-h] [--token TOKEN] --project PROJECT
                          [--with-unreleased]

    Generate CHANGELOG file.

    optional arguments:
      -h, --help         show this help message and exit
      --token TOKEN      Github token
      --project PROJECT  Github project (<owner>/<repo>)
      --with-unreleased  Include unreleased merged pull requests
