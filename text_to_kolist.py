#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2022-02-08
Purpose: Turn a copy paste of a list of KO numbers from a KEGG BRITE entry into a comma separated list ready to use (in R for example)
"""

import argparse
import sys
import re
import numpy as np
import pandas as pd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Extract the KO numbers from KEGG Brite entry',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type = argparse.FileType('rt'),
                        help='The input text file')
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output)',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Find all the instances of the regular expression of the KO number in the file"""

    args = get_args()
    pattern = 'K{1}[0-9]{5}'
        
    result = re.findall(pattern, args.file.read()) # extract the konumbers from texg

    # the following are conversions to print in correct format
    result = np.array(result)
    reshaped = result.reshape(len(result),1)
    df = pd.DataFrame(reshaped, columns=['konumber'])
    
    # this changes printing options to avoid collapse
    with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
        print(df, file=args.outfile)





    


# --------------------------------------------------
if __name__ == '__main__':
    main()
