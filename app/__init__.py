from flask import Flask

from app.views import app as bp_app


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(bp_app)

    return app
