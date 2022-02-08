#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2022-02-08
Purpose: Turn a copy paste of a list of KO numbers from a KEGG BRITE entry into a comma separated list ready to use (in R for example)
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type = argparse.FileType('rt'),
                        help='The input text file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    ko_numbers = list()

    for line in args.file.read().split():
        if line == : ## Use the re to find the KOnumbers
            ko_numbers.append(line)

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
