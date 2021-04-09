import click

from src.api import EthparserAPI
from src.parser import get_summary
from src.utils import parse_date_unix


@click.command()
@click.argument("from_date")
@click.argument("to_date")
@click.argument("ethparser_url")
def main(from_date, to_date, ethparser_url):
    api = EthparserAPI(ethparser_url)
    hardworks = api.get_hardwork_history(
        parse_date_unix(from_date), parse_date_unix(to_date)
    )
    print(get_summary(hardworks))


if __name__ == "__main__":
    main()
