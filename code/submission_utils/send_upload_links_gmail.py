from __future__ import print_function
import base64
import sys
import os.path
import pickle
import argparse
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


SCOPES = ['https://mail.google.com/']


def setup_cmdline_parser():
    parser = argparse.ArgumentParser(description='Submission system setup!')
    parser.add_argument('--subject', dest='subject', default=None, help='Email subject!')
    parser.add_argument('--student_link_file', dest='student_link_file', default=None, help='Student pickle file with link and path information')    
    parser.add_argument('--credential_file', dest='credential_file', default=None, help='JSON config with credentials (created via Google API')
    args = parser.parse_args()
    return args


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(error)

    
def main(argv):
    args = setup_cmdline_parser()
    assert args.credential_file is not None

    if not os.path.exists(args.student_link_file):
        print("File {} does not exist!".format(args.student_link_file))

    students = pickle.load( open( args.student_link_file, "rb" ) )

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(args.credential_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    service = build('gmail', 'v1', credentials=creds)

    for i,(k,v) in enumerate(students.items()):
        print("Sending {} to {} {}".format(v['link'], v['Vorname'], v['Nachname']))

        message = create_message('me', v['email'], args.subject, 'The upload link is {}'.format(v['link']))
        print(send_message(service=service, user_id='me', message=message))


if __name__ == '__main__':
    main(sys.argv)  