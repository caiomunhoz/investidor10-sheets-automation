from web_automation.session import WebSession
from web_automation.pages import LoginPage, WalletPage

def run_web_automation(entries):
    with WebSession() as driver:
        login_page = LoginPage(driver, 'https://investidor10.com.br/login')
        login_page.get_url()
        login_page.authenticate()

        wallet_page = WalletPage(driver, 'https://investidor10.com.br/wallet/my-wallet')
        wallet_page.get_url()
        wallet_page.open_entry_form()

        for entry in entries:
            wallet_page.add_entry(entry)