from config.variables import USER_WALLET_ID
from decimal import Decimal
import pendulum

def to_payload_format(row):
    return {
        'date': row[0],
        'qty': row[3],
        'cost': row[4].replace('R$ ', ''),
        'price': row[5].replace('R$ ', ''),
        'type': row[7],
        'ticker': row[8],
        'ticker_type': row[9],
        'user_wallet_id': USER_WALLET_ID,
        'source': 'MANUAL',
        'auto_conversion': 1
    }

def filter_by_current_month_purchases(rows):
    entries = []
    today = pendulum.now()

    for row in rows:
        entry_date = pendulum.from_format(row[0], 'DD/MM/YYYY')

        if entry_date.month == today.month and entry_date.year == today.year and row[7] == 'MANUAL':
            entries.append(to_payload_format(row))

    return entries