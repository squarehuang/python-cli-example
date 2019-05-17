import click
import cli_app


@click.group()
def base_cli():
    pass


@base_cli.command()
@click.option('-v', '--verbose', count=True)
def run(verbose):
    print(cli_app.joke())
    click.echo('Verbosity: {}'.format(verbose))


@base_cli.command()
@click.option('--debug/--no-debug')
def sync(debug):
    click.echo('Synching')
    click.echo('Debug mode is {}'.format('on' if debug else 'off'))


from cli_app.custom_cli import register

if __name__ == '__main__':
    base_cli()
