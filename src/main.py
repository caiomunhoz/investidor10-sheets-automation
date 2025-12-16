from google_sheets.reader import read_spreadsheet
from services.entry_service import filter_by_current_month_purchases
from services.web_automation_service import run_web_automation

def main():
    rows = read_spreadsheet(spreadsheet_range='LANÇAMENTOS!A2:K20')
    current_month_entries = filter_by_current_month_purchases(rows)

    if current_month_entries:
        run_web_automation(current_month_entries)

if __name__ == '__main__':
    main()