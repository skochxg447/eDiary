from app import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    body = db.Column(db.String(500), nullable=True)
    tags = db.Column(db.String(100), nullable=True)
    date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"{self.title} created on {self.date}"