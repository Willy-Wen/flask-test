from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import sqlite3
application = Flask(__name__)
application.config['DEBUG'] = True
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
application.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"
name = "Willy"
fruit = ["apple","banana","grape","pineapple","strawberry"]

# conn = sqlite3.connect('C:/Users/w2666/tf2/flask/web1/SQLite/test.db') # ~代表路徑
# c = conn.cursor()
# c.execute("INSERT INTO test1(name, age) VALUES ('David', 40)")
# conn.commit()
# conn.close()
@application.route("/")
@application.route("/home/")
@application.route("/home/<name>")
def home(site_name="home",name=name):
    return render_template('home.html', **locals())

@application.route("/hello/")
@application.route("/hello/<name>")
def hello(site_name="hello",name=name,fruit=fruit):
    return render_template('hello.html', **locals())

@application.route("/get", methods=['GET'])
def get(site_name="get",name=name):
    name = request.args.get('name')
    return render_template('get.html', **locals())

@application.route("/form")
def form(site_name="form",name=name):
    return render_template('form.html', **locals())

@application.route("/submit", methods=['POST'])
def submit(site_name="submit"):
    firstname = request.values['firstname']
    lastname = request.values['lastname']
    return render_template('submit.html', **locals())

@application.route("/login", methods=["POST","GET"])
def login(site_name="login"):
    if request.method == "POST":
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html", **locals())

@application.route("/user")
def user(site_name="User"):
    if "user" in session:
        user = session["user"]
        return render_template("user.html", **locals())
    else:
        return redirect(url_for("login"))

@application.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ =="__main__":
    app.run(debug=True)
