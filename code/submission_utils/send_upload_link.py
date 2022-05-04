import owncloud
import argparse
from getpass import getpass
import numpy as np
import pickle
import json
import csv
import sys
import os

from exchangelib import Account, Configuration, Credentials, Message, Mailbox, DELEGATE
from exchangelib import EWSTimeZone, EWSDateTime, EWSDate


def setup_cmdline_parser():
    parser = argparse.ArgumentParser(description='Submission system setup!')
    parser.add_argument(
        '--subject', 
        dest='subject', 
        default=None, 
        help='Email subject!')
    parser.add_argument(
        '--student_link_file', 
        dest='student_link_file', 
        default=None, 
        help='Student pickle file with link and path information')    
    parser.add_argument(
        '--config_file', 
        dest='config_file', 
        default=None, 
        help='JSON config for emails (e.g., config.json)')
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
        username = data['username']
        password = data['password']
        email = data['email']

    credentials = Credentials(username=username, password=password)
        
    a = Account(
    	primary_smtp_address=email, 
    	credentials=credentials,
        autodiscover=True, 
        access_type=DELEGATE)

    a.root.refresh()
    some_folder = a.root / 'Top of Information Store' / 'Sent Items' / 'Automatic'

    if not os.path.exists(args.student_link_file):
        print("File {} does not exist!".format(args.student_link_file))

    students = pickle.load( open( args.student_link_file, "rb" ) )
    for i,(k,v) in enumerate(students.items()):
        print("Sending {} to {} {}".format(v['link'], v['Vorname'],v['Nachname']))
        m = Message(
            account=a,
            folder=some_folder,
            subject=args.subject,
            body="({} {}): The upload link is {}".format(
                v['Vorname'],
                v['Nachname'],
                v['link']),
            to_recipients=[Mailbox(email_address=v['email'])]
        )
        print(m)
        #m.send_and_save()
        

if __name__ == '__main__':
    main(sys.argv)    
