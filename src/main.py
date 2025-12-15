from google_sheets.reader import read_spreadsheet
from services.entry_service import filter_by_current_month
from web_automation.session import WebSession
from web_automation.pages import LoginPage, WalletPage

def run_web_automation(entries):
    with WebSession() as driver:
        login_page = LoginPage(driver, 'https://investidor10.com.br/login')
        login_page.get_url()
        login_page.authenticate()

        print('Auth complete!')

        wallet_page = WalletPage(driver, 'https://investidor10.com.br/wallet/my-wallet')
        wallet_page.get_url()
        wallet_page.open_entry_form()

        print('Form opened!')

        # for i, entry in enumerate(entries[:1]):
        #     wallet_page.fill_entry_form(entry)

        #     if i < len(entries) - 1:
        #         # TODO: reopen form
        #         ...

def main():
    rows = read_spreadsheet(spreadsheet_range='LANÇAMENTOS!A2:F20')
    current_month_entries = filter_by_current_month(rows)

    if not current_month_entries:
        return

    run_web_automation(current_month_entries)

if __name__ == '__main__':
    main()