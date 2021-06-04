import click
from flask import current_app
from flask.cli import with_appcontext

def setup():
    from portfolio.models import engine, metadata
    metadata.create_all(engine)

@click.command("init-db")
@with_appcontext
def init_db():
    setup()

def test_db():
    setup()
    