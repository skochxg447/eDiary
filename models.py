from app import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"{self.title} created on {self.date}"

# def init_db():
#     db.create_all()

#     # Create a test user
#     new_user = User('a@a.com', 'aaaaaaaa')
#     new_user.display_name = 'Nathan'
#     db.session.add(new_user)
#     db.session.commit()

#     new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
#     db.session.commit()


# if __name__ == '__main__':
#     init_db()