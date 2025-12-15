from config.variables import USER_WALLET_ID
import pendulum

def to_payload_format(row):
    return {
        'date': row[0],
        'qty': int(row[3]),
        'price': float(row[4]),
        'ticker': row[6],
        'type': row[7],
        'cost': float(row[8]),
        'user_wallet_id': USER_WALLET_ID,
        'source': 'MANUAL',
        'auto_conversion': 1,
        'ticker_type': 'Ticker'
    }

def filter_by_current_month(rows):
    entries = []
    today = pendulum.now()

    for row in rows:
        entry_date = pendulum.from_format(row[0], 'DD/MM/YYYY')

        if entry_date.month == today.month and entry_date.year == today.year:
            entries.append(to_payload_format(row))

    return entries