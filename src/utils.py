from datetime import datetime
import locale

def parse_date_unix(date) -> int:
    return int(datetime.strptime(date, "%d/%m/%Y").timestamp())

def format_currency(amount):
    locale.setlocale( locale.LC_ALL, '' )
    return locale.currency(amount, grouping=True )

def format_number(number):
    return '{:0,.2f}'.format(number)