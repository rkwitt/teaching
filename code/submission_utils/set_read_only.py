import owncloud
import argparse
import numpy as np
import pickle
import json
import csv
import sys
import os

from utils import read_students, read_students_exam

def setup_cmdline_parser():
    parser = argparse.ArgumentParser(description='Set permissions to READ-ONLY!')
    parser.add_argument(
        '--root', 
        dest='root', 
        default=None, 
        help='e.g., /Uploads/ML-10/ExA')
    parser.add_argument(
        '--config_file', 
        dest='config_file', 
        default=None, 
        help='JSON config file (e.g., config.json)')
    parser.add_argument(
        '--exam', 
        dest='exam', 
        action='store_true',
        default=False, 
        help='Reading students from an exam registration export in PLUS Online')
    parser.add_argument(
        '--student_file', 
        dest='student_file', 
        default=None, 
        help='Student CSV file from PLUS Online')
    parser.add_argument(
        '--student_link_file', 
        dest='student_link_file', 
        default=None, 
        help='Student pickle file with link and path information')
    
    args = parser.parse_args()
    return args


def _update_share(oc, path):
    link_info = oc.share_file_with_link(path)
    oc.update_share(link_info.get_id(), perms=oc.OCS_PERMISSION_READ)
    return link_info.get_link()

def main(argv):
    args = setup_cmdline_parser()

    assert args.root is not None
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

    groups = {}
    for k,v in students.items():
        if 'group' in v:
            groups[v['group']] = None

    for k,v in students.items():
        if 'group' in v:
            if groups[v['group']] is None:
                share_list = oc.get_shares(v['path'])
                if len(share_list)>0:
                    oc.delete_share(share_list[0].get_id())
                link = _update_share(oc, v['path'])
                v['read_only_link'] = link
                groups[v['group']] = link
            else:
                v['read_only_link'] = groups[v['group']]
        else:
            share_list = oc.get_shares(v['path'])
            if len(share_list)>0:
                oc.delete_share(share_list[0].get_id())
            link = _update_share(oc, v['path'])
            v['read_only_link'] = link

    pickle.dump( students, open( args.student_link_file, "wb" ) )


if __name__ == '__main__':
    main(sys.argv)
