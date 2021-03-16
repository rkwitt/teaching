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
    parser = argparse.ArgumentParser(description='Submission system setup!')
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
        '--out_file', 
        dest='out_file', 
        default=None, 
        help='Output file with upload links')

    args = parser.parse_args()
    return args


def check_group(students):
    group_ids = np.array([int(v['group']) for k,v in students.items()])
    use_group = np.all(group_ids>=0)
    if use_group:
        print('Using {:d} groups'.format(len(np.unique(group_ids))))
    return use_group, np.unique(group_ids)

def _create_dir(oc, path):
    try:
        oc.mkdir(path)
    except owncloud.owncloud.HTTPResponseError:
        print('could not create {}!'.format(path))
        sys.exit(-1)


def _share(oc, path):
    link_info = oc.share_file_with_link(path)
    # create public upoad link - IF NOT WANTED, just use perms=....
    oc.update_share(link_info.get_id(), public_upload=True) #perms=oc.OCS_PERMISSION_SHARE)
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

    if not os.path.exists(args.student_file):
        print('Student file {} not found!'.format(args.student_file))
        sys.exit(-1)

    if args.exam:
        students = read_students_exam(args.student_file)
    else:
        students = read_students(args.student_file)

    use_group, group_ids = check_group(students)

    group_dirs = None
    if use_group:
        group_dirs = {g: 
            {
                'path': os.path.join(args.root, 'group_{:02d}'.format(g)), 
                'created': False,
                'link': None
            } for g in group_ids}

    for k,v in students.items():
        if use_group:
            group_id = v['group']
            if not group_dirs[group_id]['created']:
                _create_dir(oc, group_dirs[group_id]['path'])
                link = _share(oc, group_dirs[group_id]['path'])
                group_dirs[group_id]['created']=True
                group_dirs[group_id]['link']=link
                v['link'] = link
            else:
                v['link'] = group_dirs[group_id]['link']
            v['path'] = group_dirs[group_id]['path']
        else:
            student_dir = os.path.join(args.root, '{}'.format(str(k)))
            _create_dir(oc, student_dir)
            link = _share(oc, student_dir)
            v['link'] = link
            v['path'] = student_dir
    
    if args.out_file is not None:
        pickle.dump( students, open( args.out_file, "wb" ) )
    

if __name__ == '__main__':
    main(sys.argv)
