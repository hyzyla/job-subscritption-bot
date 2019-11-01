from flask import Flask


def create_app():
    app = Flask(__name__.split(".")[0])
    # app.config.from_object(config_object)
    return app
