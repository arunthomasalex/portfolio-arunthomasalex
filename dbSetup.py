import click
from flask.cli import with_appcontext

def setup():
    from sqlalchemy import create_engine
    from portfolio.models import Base, engine
    Base.metadata.create_all(engine)


@click.command("init-db")
@with_appcontext
def init_db():
    setup()

def test_db():
    setup()
    