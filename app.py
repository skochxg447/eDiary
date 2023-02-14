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
import sqlite3
import tkinter as tk 

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

from forms import AddEntryForm
from forms import DeleteEntryForm
import models

# from routes import *
@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect('instance/data.db')
    cur = conn.cursor()
    entries = cur.execute('''SELECT * FROM entry''')
    lst = entries.fetchall()


    if request.method == 'POST':
        form = AddEntryForm()

        title = request.form['title']
        body = request.form['body']
        tags = request.form['tags']
    
        entry = models.Entry(title=form.title.data, 
            body=form.body.data, 
            tags=form.tags.data, 
            date=datetime.utcnow())
        db.create_all()
        db.session.add(entry)
        db.session.commit()
        flash("Entry added")
    return render_template('index.html', lst=lst)

@app.route("/submit_form", methods=["GET", "POST"])
def submit_form():

    if request.method == 'POST':
        form = AddEntryForm()

        title = request.form['title']
        body = request.form['body']
    
        entry = models.Entry(title=form.title.data, body=form.body.data, tags=form.tags.data, date=datetime.utcnow())
        db.session.add(entry)
        db.session.commit()
        flash("Entry added")
        return redirect(url_for("index"))
    return render_template('index.html', entries=entries)

# @app.route("/list", methods=["GET", "POST"])
# def list_data():
#     entries = models.Entry.query.all()
#     conn = sqlite3.connect('data.db')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM entry')
#     data = cur.fetchall()
#     conn.close()
#     return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
