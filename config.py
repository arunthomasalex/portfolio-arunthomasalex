import os
class Config(object):
    TESTING = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_QUERY = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DATABASE_NAME = "postgres"
    SHOW_QUERY = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////home/arunalex/portfolio-arunthomasalex/instance/portfolio.db"

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:////home/arunalex/portfolio-arunthomasalex/instance/portfolio.db"
    TESTING = True