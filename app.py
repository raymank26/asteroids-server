from __future__ import absolute_import
import os

from flask import Flask, render_template, g
from api.users import users
from api.scores import scores
from flask.ext.mongoengine import MongoEngine

def create_app(override=None):
    app = Flask(__name__)
    app.config.from_pyfile(
        os.environ.get("FLASK_ASTEROIDS_CONFIG", "config/local.py")
    )
    if override:
        app.config.update(override)

    db = MongoEngine(app)

    @app.before_request
    def before_request():
        g.mongo = db

    # register blueprints
    app.register_blueprint(users)
    app.register_blueprint(scores)
    @app.route("/")
    def base():
        return render_template("base.html")

    return app, db




if __name__ == "__main__":
    app, db = create_app()
    app.run()
    # connection.register([User])
