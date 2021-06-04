class Config(object):
    TESTING = False
    SCHEMA_FILE = "sqlite_schema.sql"
    DATABASE_NAME = "sqlite"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgres://waisfcqduxnsko:1bead801de26055d93c3e6b6444b05f7443b33252f346d55dcd2ed133ae2400a@ec2-52-21-252-142.compute-1.amazonaws.com:5432/dde1t0r3k0v5bt"
    SCHEMA_FILE = "postgres_schema.sql"
    DATABASE_NAME = "postgres"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////home/arunalex/portfolio-arunthomasalex/instance/portfolio.db"
    DATABASE_URL = "portfolio.db"

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////home/arunalex/portfolio-arunthomasalex/instance/portfolio.db"
    DATABASE_URL = "portfolio.db"
    TESTING = True