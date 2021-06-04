import os
class Config(object):
    TESTING = False
    SCHEMA_FILE = "sqlite_schema.sql"
    DATABASE_NAME = "sqlite"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SCHEMA_FILE = "postgres_schema.sql"
    DATABASE_NAME = "postgres"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////home/arunalex/portfolio-arunthomasalex/instance/portfolio.db"
    DATABASE_URL = "portfolio.db"

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////home/arunalex/portfolio-arunthomasalex/instance/portfolio.db"
    DATABASE_URL = "portfolio.db"
    TESTING = True