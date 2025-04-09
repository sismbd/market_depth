import pickle
import os
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Load credentials
with open('token.pickle', 'rb') as token:
    creds = pickle.load(token)

service = build('drive', 'v3', credentials=creds)

# Use the DRIVE_FOLDER_ID from environment variables
folder_id = os.environ.get('DRIVE_FOLDER_ID')

# Example: List files in the folder
results = service.files().list(
    q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(f"{item['name']} ({item['id']})")
