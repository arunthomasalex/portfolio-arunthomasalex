import os
import logging
import dbSetup
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

def index():
    return jsonify(dict(
        test="Hello World!"
    ))

def create_app(test_config = None):
    app = Flask(__name__, static_folder='static', static_url_path='/', instance_relative_config=True)
    if test_config is None:
        app.config.from_object(f"config.{app.config['ENV'].capitalize()}Config")
    else:
        app.config.from_object(f"config.{test_config['ENV'].capitalize()}Config")
    CORS(app, resources={r"/*": {"origins": "*"}})
    try:
        os.makedirs(app.instance_path) # Create instance path for the local db and log file creation
    except OSError:
        pass
    app.cli.add_command(dbSetup.init_db) # Register cli command "flask init-db"
    logging.basicConfig(filename=f"{app.instance_path}/portfolio.log", level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(threadName)s : %(message)s")
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
        app.add_url_rule("/", 'index', index)
    return app