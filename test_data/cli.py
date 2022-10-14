import click
from test_data.app import start as start_app


@click.command("stock-winners")
def start():
    start_app()

