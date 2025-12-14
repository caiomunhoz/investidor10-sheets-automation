from google.oauth2.service_account import Credentials
import json

def get_credentials(GOOGLE_CLOUD_CREDENTIALS_JSON):
    USER_INFO = json.loads(GOOGLE_CLOUD_CREDENTIALS_JSON)
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    return Credentials.from_service_account_info(USER_INFO, scopes=SCOPES)