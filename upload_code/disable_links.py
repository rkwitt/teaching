import owncloud
import argparse
import numpy as np
import pickle
import json
import csv
import sys
import os


def setup_cmdline_parser():
    parser = argparse.ArgumentParser(description='Submission system setup!')
    parser.add_argument(
        '--student_link_file', 
        dest='student_link_file', 
        default=None, 
        help='Student pickle file with link and path information')
    parser.add_argument(
        '--config_file', 
        dest='config_file', 
        default=None, 
        help='JSON config file (e.g., config.json)')
    args = parser.parse_args()
    return args


def main(argv):
    args = setup_cmdline_parser()

    assert args.config_file is not None
    if not os.path.exists(args.config_file):
        print('Config file {} not found!'.format(args.config_file))
        sys.exit(-1)
        
    with open(args.config_file) as json_file:
        data = json.load(json_file)
        url = data['url']
        login = data['user']
        app_key = data['app_key']

    oc = owncloud.Client(url)
    oc.login(login, app_key)

    students = pickle.load( open( args.student_link_file, "rb" ) )
    for k,v in students.items():        
        share_list = oc.get_shares(v['path'])
        if len(share_list)>0:
            oc.delete_share(share_list[0].get_id())
        

if __name__ == '__main__':
    main(sys.argv)
