from google_sheets.reader import read_spreadsheet
from services.entry_service import filter_by_current_month_purchases
from web_automation.session import WebSession
from web_automation.pages import LoginPage, WalletPage

def main():
    rows = read_spreadsheet(spreadsheet_range='LANÇAMENTOS!A2:J20')
    current_month_entries = filter_by_current_month_purchases(rows)

    if not current_month_entries:
        return

    with WebSession() as driver:
        login_page = LoginPage(driver, 'https://investidor10.com.br/login')
        login_page.get_url()
        login_page.authenticate()

        wallet_page = WalletPage(driver, 'https://investidor10.com.br/wallet/my-wallet')
        wallet_page.get_url()
        wallet_page.open_entry_form()

        for entry in current_month_entries:
            wallet_page.add_entry(entry)

if __name__ == '__main__':
    main()