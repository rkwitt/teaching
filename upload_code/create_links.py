import owncloud
import argparse
import numpy as np
import json
import csv
import sys
import os


def setup_cmdline_parser():
    parser = argparse.ArgumentParser(description='Submission system setup!')
    parser.add_argument('--root', dest='root', default=None, help='e.g., /Uploads/ML-10/')
    parser.add_argument('--config_file', dest='config_file', default=None, help='JSON config file (e.g., config.json)')
    parser.add_argument('--num_groups', type=int, dest='num_groups', default=-1, help='Number of groups to create')
    parser.add_argument('--out_file', dest='out_file', default=None, help='Output file with upload links')
    args = parser.parse_args()
    return args


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

    write_to_csv = False
    if args.out_file is not None:
        out_fid = open(args.out_file, mode='w')
        out_writer = csv.writer(out_fid, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_to_csv = True

    assert args.num_groups > 0 
    for g in np.arange(args.num_groups):
        group_dir = os.path.join(args.root, 'group_{:02d}/'.format(g))
        print(group_dir)
        try:
            oc.mkdir(group_dir)
        except owncloud.owncloud.HTTPResponseError:
            print('could not create {}!'.format(group_dir))

        link_info = oc.share_file_with_link(group_dir)
        oc.update_share(link_info.get_id(), perms=oc.OCS_PERMISSION_CREATE)
        
        if write_to_csv:
            out_writer.writerow(['group_{:02d}'.format(g), link_info.get_link()])
        else:
            print(['group_{:02d}'.format(g), link_info.get_link()])
    

if __name__ == '__main__':
    main(sys.argv)
