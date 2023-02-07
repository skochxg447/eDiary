from app import app, db
from flask import (
    render_template,
    url_for,
    flash,
    get_flashed_messages,
    redirect,
    request,
)
from datetime import datetime

import models
import forms

def add(x, y):
    return x + y

@app.route("/")
@app.route("/index")


def index():
    entries = models.Entry.query.all()
    return render_template("index.html", entries=entries)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = forms.AddEntryForm()
    if form.validate_on_submit():
        entry = models.Entry(title=form.title.data, date=datetime.utcnow())
        db.session.add(entry)
        db.session.commit()
        flash("Entry added")
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:entry_id>", methods=["GET", "POST"])
def edit(entry_id):
    form = forms.AddEntryForm()
    entry = models.Entry.query.get(entry_id)
    print(entry)
    if entry:
        if form.validate_on_submit():
            entry.title = form.title.data
            entry.date = datetime.utcnow()
            db.session.commit()
            flash("Entry updated")
            return redirect(url_for("index"))
        form.title.data = entry.title
        return render_template("edit.html", form=form, entry_id=entry_id)
    flash(f"Entry with id {entry_id} does not exit")
    return redirect(url_for("index"))


@app.route("/delete/<int:entry_id>", methods=["GET", "POST"])
def delete(entry_id):
    form = forms.DeleteEntryForm()
    entry = models.Entry.query.get(entry_id)
    if entry:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(entry)
                db.session.commit()
                flash("Entry deleted")
            return redirect(url_for("index"))
        return render_template(
            "delete.html", form=form, entry_id=entry_id, title=entry.title
        )
    flash(f"Entry with id {entry_id} does not exit")
    return redirect(url_for("index"))
