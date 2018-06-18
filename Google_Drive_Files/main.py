
from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES, CLIENT_SECRET_FILE, APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

def listFiles(size):
    results = drive_service.files().list(
        pageSize=size,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('FILES in Google Drive:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

def uploadFile(filename, filepath, mimetype):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath,
                            mimetype=mimetype)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))


def downloadFile(file_id, filepath):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(filepath, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())
        
def createFolder(name):
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print('Folder ID: %s' % file.get('id'))    
        
def searchFile(size, query):
    results = drive_service.files().list(
    pageSize=size,fields="nextPageToken, files(id, name, kind, mimeType)", q=query).execute()
    # Search parameters: https://developers.google.com/drive/api/v3/search-parameters.
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Found FILES in Google Drive:')
        for item in items:
            print(item)
            #print('{0} ({1})'.format(item['name'], item['id']))    
            # Can comment line above.

#listFiles(1000)
#    uncomment line above to display list of your files in G.drive.

#uploadFile('wallpapers (35).jpg', 'wallpapers (35).jpg', 'image/jpg')
#    uncomment line above to upload file, the file had to be storage in your work folder.

#downloadFile('1Yu7BKFTmoJNFbiJHyPjAs8PMbO6h4n-v', '12.jpg')
#    uncomment line above to download file ('FILE_id', 'fileNAME').

#createFolder('Test_Folder_NEW')
#    uncomment line above to create folder ('folderNAME').

searchFile(100, "name contains 'FIRST'")
#    uncomment line above to search file ('fileCount_to_display', "name contain 'WORD_in_file_name'").