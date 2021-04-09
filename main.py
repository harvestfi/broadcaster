import click

from src.api import EthparserAPI
from src.parser import get_summary
from src.utils import parse_date_unix
from src.infographic import InfographicGenerator

@click.command()
@click.argument("from_date")
@click.argument("to_date")
@click.argument("ethparser_url")
def main(from_date, to_date, ethparser_url):
    api = EthparserAPI(ethparser_url)
    hardworks = api.get_hardwork_history(
        parse_date_unix(from_date), parse_date_unix(to_date)
    )
    hardwork_summary = get_summary(hardworks)

    print(hardwork_summary)

    ig = InfographicGenerator()
    ig.generate_infographic(hardwork_summary)



if __name__ == "__main__":
    main()
