
import click
from cli_app.cli import base_cli


@base_cli.command()
@click.option('--username')
def register(username):
    click.echo("hello there")
    click.echo('Hello %s!' % username)
