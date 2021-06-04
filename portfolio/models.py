from flask import current_app
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"])
metadata = MetaData()

Message = Table("messages", metadata,
    Column("id", Integer, primary_key = True),
    Column("name", String(20), nullable = False),
    Column("email", String(100), nullable = False),
    Column("subject", String(100), nullable = False),
    Column("message", String(500), nullable = False)
)