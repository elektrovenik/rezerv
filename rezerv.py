# coding=utf-8
__author__ = 'kid'

# how use example:
# pip install dropbox
# wget https://github.com/elektrovenik/rezerv/raw/master/rezerv.py
# python2.7 ~/sh/rezerv.py -chunk=100000 -auth-file=/home/backup/sh/.token $BACKUP_DIR/last/postgresql.sql.gz.7z  postgresql.sql.gz.7z

from dropbox.client import DropboxOAuth2FlowNoRedirect, DropboxClient
import argparse
import os
from dropbox import rest as dbrest


def get_access_token(auth_info_file):
    import json

    try:
        with open(auth_info_file, 'r') as f:
            j = f.read()
            f.close()
            j = json.loads(j)
            return j['access_token']

    except Exception, e:
        auth_flow = DropboxOAuth2FlowNoRedirect('qav1kg293h4er4s', 'oidwgvr0tiqjlf1')

        authorize_url = auth_flow.start()
        print "1. Go to: " + authorize_url
        print "2. Click \"Allow\" (you might have to log in first)."
        print "3. Copy the authorization code."
        auth_code = raw_input("Enter the authorization code here: ").strip()

        try:
            access_token, user_id = auth_flow.finish(auth_code)
            print('Token: %s' % access_token)
            print('UserID: %s' % user_id)

            with open(auth_info_file, 'w') as f:
                f.write(json.dumps({'access_token': access_token, 'user_id': user_id}))
                f.close()

            return access_token

        except dbrest.ErrorResponse, e:
            print('Error: %s' % (e,))


default_chunk_size = 1 * 1000 * 1000

parser = argparse.ArgumentParser(description='Rotate old backup files by date.')
parser.add_argument('file_path', metavar='<file_path>', type=str, help='path to file for backup')
parser.add_argument('dropbox_path', metavar='<file_path>', type=str, help='path on dropbox fs for save backup')
parser.add_argument('--silent', action='store_true', default=False, help='don`t print revisions table')
parser.add_argument('-auth-file', metavar='auth file', type=str, default='./.token',
                    help='place of file auth dropbox with token')
parser.add_argument('-chunk', metavar='chunk', type=int, default=default_chunk_size, help='chunk size')

args = parser.parse_args()

file_path = args.file_path
dropbox_path = args.dropbox_path

auth_file = os.path.join(os.getcwd(), '.token') if args.auth_file == './.token' else args.auth_file
c = DropboxClient(get_access_token(auth_file))


file_for_upload = open(file_path, 'rb')

fileSize = os.path.getsize(file_path)
if (fileSize < default_chunk_size) and (args.chunk == default_chunk_size):
    file_info = c.put_file(dropbox_path, file_for_upload, True)
else:
    uploader = c.get_chunked_uploader(file_for_upload, fileSize)
    while uploader.offset < fileSize:
        try:
            upload = uploader.upload_chunked(args.chunk)
        except dbrest.ErrorResponse, e:
            print e
    file_info = uploader.finish(dropbox_path, True)


print '%s | %10s - uploaded now' % (file_info['modified'], file_info['size'])
if not args.silent:
    for rev in c.revisions(dropbox_path):
        print '%s | %10s ' % (rev['modified'], rev['size'])
