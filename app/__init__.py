"""creates an instance of a flask application and runs it"""
from flask import Flask


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    from .api.v1.views.views import api as version1
    app.register_blueprint(version1, url_prefix='/api/v1')
    return app