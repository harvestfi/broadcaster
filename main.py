import click

from src.api import EthparserAPI
from src.parser import get_hardworks_summary, get_ps_summary
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
    ps_history = api.get_ps_history(
        parse_date_unix(from_date), parse_date_unix(to_date)
    )

    hardwork_summary = get_hardworks_summary(hardworks)
    ps_summary = get_ps_summary(ps_history)

    print(hardwork_summary)
    print(ps_summary)

    ig = InfographicGenerator()
    ig.generate_infographic(hardwork_summary, ps_summary, from_date, to_date)



if __name__ == "__main__":
    main()
