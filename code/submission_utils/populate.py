from shutil import copyfile
import owncloud
import argparse
import numpy as np
import pickle
import json
import glob
import csv
import sys
import os


def setup_cmdline_parser():
    parser = argparse.ArgumentParser(description='Populate reviews back to student directories')
    parser.add_argument(
        '--exercise_dir', 
        dest='exercise_dir', 
        default=None, 
        help='Base directory of student submissions, e.g., /tmp/ExA')
    parser.add_argument(
        '--review_dir', 
        dest='review_dir', 
        default=None, 
        help='Base directory of reviews (with same files), e.g., /tmp/ExA_review')
    args = parser.parse_args()
    return args


def main(argv):
    args = setup_cmdline_parser()

    assert os.path.exists(args.review_dir)
    assert os.path.exists(args.exercise_dir)
    
    lst_org = glob.glob(os.path.join(args.exercise_dir, '*'))
        
    # go through student submission dirs
    for l in lst_org:
        # construct mathing review directories
        match_dir = os.path.join(args.review_dir, os.path.basename(l))
        
        if os.path.exists(match_dir):

            # get all files in review dir
            to_copy = glob.glob(os.path.join(match_dir, '*'))

            # rename and copy files
            for f in to_copy:
                tmp, ext = os.path.splitext(os.path.basename(f))
                rev_file = tmp + '_review' + ext
                copyfile(f, os.path.join(l, rev_file))
                print('{} -> {}'.format(f, os.path.join(l, rev_file)))
        else:
            print('{} not found!'.format(match_dir))
    
if __name__ == '__main__':
    main(sys.argv)
