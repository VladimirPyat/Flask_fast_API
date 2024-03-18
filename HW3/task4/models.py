from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UsersDB(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f'id{self.user_id}({self.first_name, self.last_name, self.email})'






