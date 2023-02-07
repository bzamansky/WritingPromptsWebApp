import flask
import os
from flask_sqlalchemy import SQLAlchemy
import api

app = flask.Flask(__name__)
app.secret_key = "blahbbb"
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'databse.db')
app.config["SQLALCHEMY_BINDS"] = {
    'users':  'sqlite:///' + os.path.join(basedir, 'users.db'),
    'writing':  'sqlite:///' + os.path.join(basedir, 'writing.db')
}


db = SQLAlchemy(app)

class UserData(db.Model):
    __bind_key__ = 'users'
    username = db.Column(db.String(120), primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    
class WritingData(db.Model):
    __bind_key__ = 'writing'
    id = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(120))
    prompt = db.Column(db.String(500))
    writing = db.Column(db.String(1000))
    
with app.app_context():
    db.create_all()

@app.route("/", methods=['GET','POST'])
def main():
    prompt = api.initialPrompt()

    if 'user' in flask.session:
        if flask.request.form.get('logout'):
            flask.session.pop('user',None)
            return flask.render_template("index.html", loggedIn=False, prompt=prompt)

        return flask.render_template("index.html", loggedIn=True, prompt=prompt)
    elif flask.request.method == "POST":
        username = flask.request.form.get("usernameLogin")
        password = flask.request.form.get("passwordLogin")

        hasAccount = UserData.query.filter_by(username=username, password=password).first()
        if hasAccount is not None:
            flask.session['user'] = username
            return flask.render_template("profile.html",  loggedIn=True, username=username)
        return flask.render_template("index.html", loggedIn=False, loginError=True, prompt=prompt)
    return flask.render_template("index.html", loggedIn=False, prompt=prompt, bmi_data="this will be data")


@app.route("/profile")
def profile():
    return flask.render_template("profile.html")


@app.route("/signup")
def signup():
    return flask.render_template("signup.html")


@app.route("/writing")
def writing():
    return flask.render_template("writing.html")

app.run(debug=True)