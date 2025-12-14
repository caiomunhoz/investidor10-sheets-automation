from config.variables import GOOGLE_CLOUD_CREDENTIALS_JSON, SPREADSHEET_ID
from .auth import get_credentials
from .client import get_sheets_client

def read_spreadsheet(spreadsheet_range):
    credentials = get_credentials(GOOGLE_CLOUD_CREDENTIALS_JSON)
    service = get_sheets_client(credentials)

    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=spreadsheet_range)
        .execute()
    )
    
    return result.get('values', [])