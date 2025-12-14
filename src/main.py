import pendulum
from google_sheets.reader import read_spreadsheet
from web_automation.session import WebSession
from web_automation.pages import LoginPage

def get_current_month_purchases(rows):
    purchases = []
    today = pendulum.now()
    
    for row in rows:
        purchase_date = pendulum.from_format(row[0], 'DD/MM/YYYY')
        
        if purchase_date.month == today.month and purchase_date.year == today.year:
            purchases.append({
                'date': row[0],
                'asset': row[1],
                'type': row[2],
                'quantity': row[3],
                'unit_price': row[4]
            })
        
    return purchases

def run_web_automation():
    with WebSession() as driver:
        home_page = LoginPage(driver, 'https://investidor10.com.br/login')
        home_page.get_url()
        home_page.authenticate()

def main():
    rows = read_spreadsheet(spreadsheet_range='LANÇAMENTOS!A2:F20')
    current_month_purchases = get_current_month_purchases(rows)

    if not current_month_purchases:
        return

    run_web_automation()

if __name__ == '__main__':
    main()