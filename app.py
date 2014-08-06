from __future__ import absolute_import
import os

from flask import Flask, render_template
from api.users import users
from api.scores import scores
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_pyfile(
    os.environ.get("FLASK_ASTEROIDS_CONFIG", "config/local.py")
)

# ext config
db = MongoEngine(app)

# register blueprints
app.register_blueprint(users)
app.register_blueprint(scores)


@app.route("/")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run()
    # connection.register([User])
