from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_CLOUD_CREDENTIALS_JSON = os.getenv('GOOGLE_CLOUD_CREDENTIALS_JSON')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')