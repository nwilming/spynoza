import argparse
import os
import os.path as op
from spynoza.BIDS_tools import BIDSConstructor

parser = argparse.ArgumentParser(description='This is a command line tool to convert ''
                                             'unstructured data-directories to a BIDS-compatible '
                                             'format.')
parser.add_argument('-d', '--directory', help='Directory to be converted.', required=False)
parser.add_argument('-c', '--config_file', help='Config-file with img. acq. parameters', required=False)
parser.add_argument('-p', '--parallel', help='Execute par/rec conversion+zipping in parallel?',
                    required=False, type=int)

args = parser.parse_args()

if args.directory is None:
    args.directory = os.getcwd()

if args.config_file is None:
    args.config_file = op.join(os.getcwd(), 'config.json')

if args.parallel is None:
    args.parallel = -1

bids_constructor = BIDSConstructor(args.directory, args.config_file)
bids_constructor.convert2bids(args.parallel)