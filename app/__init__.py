"""creates an instance of a flask application and runs it"""
from flask import Flask, Blueprint
from instance.config import config


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    

    from .api.v1.views.views import api as version1
    app.register_blueprint(version1, url_prefix='/api/v1')
    return app