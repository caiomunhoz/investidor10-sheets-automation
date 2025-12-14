from googleapiclient.discovery import build

def get_sheets_client(credentials):
    return build('sheets', 'v4', credentials=credentials)