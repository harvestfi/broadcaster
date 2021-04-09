from datetime import datetime


def parse_date_unix(date) -> int:
    return int(datetime.strptime(date, "%d/%m/%Y").timestamp())
