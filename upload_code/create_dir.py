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
    parser.add_argument('--dir', dest='dir', default=None, help='Create directory within root!')
    args = parser.parse_args()
    return args


def main(argv):
    args = setup_cmdline_parser()

    assert args.root is not None
    assert args.config_file is not None
    assert args.dir is not None

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

    try:
        oc.mkdir(os.path.join(args.root, args.dir))
    except owncloud.owncloud.HTTPResponseError:
        print('could not create {}!'.format(args.dir))


if __name__ == '__main__':
    main(sys.argv)