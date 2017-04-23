import argparse

from printers import MarkdownPrinter
from feeds import GithubFeed


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate CHANGELOG file.'
    )
    parser.add_argument(
        '-t', '--token',
        type=str,
        help='Github token'
    )
    parser.add_argument(
        '-p', '--project',
        type=str,
        required=True,
        help='Github project (<owner>/<repo>)'
    )
    parser.add_argument(
        '--with-unreleased',
        default=False,
        action='store_true',
        help='Include unreleased merged pull requests'
    )

    return parser.parse_args()


def main():
    args = parse_args()
    timeline = GithubFeed(args.project, args.token).fetch()

    printer = MarkdownPrinter(timeline, with_unreleased=args.with_unreleased)
    printer.pretty_print()

if __name__ == '__main__':
    main()
