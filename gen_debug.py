#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse
from amtutils import *


def parse_arguments():
    """Parses the arguments passed on invocation in a dict and return it"""
    parser = argparse.ArgumentParser(description="A tool to resolve dummy conflicts")

    parser.add_argument('-m', '--merged', required=True)
    parser.add_argument(
        '-r',
        '--report',
        choices=[REPORT_NONE, REPORT_SOLVED, REPORT_UNSOLVED, REPORT_FULL],
        default=REPORT_UNSOLVED,
        required=False)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    walker = ConflictsWalker(args.merged, 'mwc', args.report)
    while walker.has_more_conflicts():
        continue
    walker.end()
    sys.exit(walker.get_merge_status())
