import click

from src.api import EthparserAPI
from src.parser import get_hardworks_summary, get_ps_summary, get_vaults_summary
from src.utils import parse_date_unix
from src.infographic import InfographicGenerator


@click.group()
def cli1():
    pass

@cli1.command()
@click.argument("from_date")
@click.argument("to_date")
@click.argument("ethparser_url")
def strategies_infographic(from_date, to_date, ethparser_url):
    api = EthparserAPI(ethparser_url)

    hardworks = api.get_hardwork_history(
        parse_date_unix(from_date), parse_date_unix(to_date)
    )
    ps_history = api.get_ps_history(
        parse_date_unix(from_date), parse_date_unix(to_date)
    )
    vaults_info = api.get_vaults(
        "eth"
    )

    hardwork_summary = get_hardworks_summary(hardworks)
    ps_summary = get_ps_summary(ps_history)
    vaults_summary = get_vaults_summary(vaults_info)

    print(hardwork_summary)
    print(ps_summary)
    print(vaults_summary)

    ig = InfographicGenerator()
    ig.generate_strategies_infographic(hardwork_summary, ps_summary, vaults_summary, from_date, to_date)

@cli1.command()
@click.argument("from_date")
@click.argument("to_date")
@click.argument("ethparser_url")
def users_infographic(from_date, to_date, ethparser_url):
    api = EthparserAPI(ethparser_url)

    hardworks = api.get_hardwork_history(
        parse_date_unix(from_date), parse_date_unix(to_date)
    )
    ps_history = api.get_ps_history(
        parse_date_unix(from_date), parse_date_unix(to_date)
    )
    vaults_info = api.get_vaults(
        "eth"
    )

    hardwork_summary = get_hardworks_summary(hardworks)
    ps_summary = get_ps_summary(ps_history)
    vaults_summary = get_vaults_summary(vaults_info)

    print(hardwork_summary)
    print(ps_summary)
    print(vaults_summary)

    ig = InfographicGenerator()
    ig.generate_users_infographic(hardwork_summary, ps_summary, vaults_summary, from_date, to_date)

@cli1.command()
def main():
    pass

cli = click.CommandCollection(sources=[cli1])

if __name__ == '__main__':
    cli()