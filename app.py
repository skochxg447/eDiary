from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import (
    render_template,
    url_for,
    flash,
    get_flashed_messages,
    redirect,
    request,
)
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

import forms
# from routes import *
@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    # if request.method == 'POST':
    #     title = request.form['title']
    #     body = request.form['body']
    
    #     entry = models.Entry(title=form.title.data, body=form.body.data, date=datetime.utcnow())
    #     db.session.add(entry)
    #     db.session.commit()
    #     flash("Entry added")
    #     return redirect(url_for("index"))
    return render_template('index.html')

@app.route("/submit_form", methods=["GET", "POST"])
def submit_form():
    title = request.form['title']
    body = request.form['body']
    if request.method == 'POST':
        entry = models.Entry(title=form.title.data, body=form.body.data, date=datetime.utcnow())
        db.session.add(entry)
        db.session.commit()
        flash("Entry added")
        return redirect(url_for("index"))

    return 'Form submitted successfully!'

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
