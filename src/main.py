import pendulum
from google_sheets.reader import read_spreadsheet
from web_automation.session import WebSession
from web_automation.pages import LoginPage, WalletPage

def get_current_month_entries(rows):
    entries = []
    today = pendulum.now()

    for row in rows:
        entry_date = pendulum.from_format(row[0], 'DD/MM/YYYY')

        if entry_date.month == today.month and entry_date.year == today.year:
            entries.append({
                'date': row[0],
                'asset': row[1],
                'asset_type': row[2],
                'quantity': row[3],
                'price': row[4]
            })
  
    return entries

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
    current_month_entries = get_current_month_entries(rows)

    if not current_month_entries:
        return

    run_web_automation(current_month_entries)

if __name__ == '__main__':
    main()