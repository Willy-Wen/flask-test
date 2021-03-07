from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

application = Flask(__name__)
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@application.route('/')
def home(site_name="home"):
    return render_template('home.html', **locals())

if __name__ =="__main__":
    application.run(debug=True)