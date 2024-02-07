from db import DB
from passlib.hash import pbkdf2_sha256


class UserModel(DB.Model):
    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(100), nullable=False, unique=True)
    password = DB.Column(DB.String(300), nullable=False)

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = pbkdf2_sha256.hash(password)

    def as_dict(self):
        return {
            'id': self.id,
            'email': self.email
        }

    @classmethod
    def find_user_by_email(cls, _email):
        return cls.query.filter_by(email=_email).first()

    def save(self):
        DB.session.add(self)
        DB.session.commit()
