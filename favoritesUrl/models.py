from favoritesUrl.ext.database import db
from sqlalchemy_serializer import SerializerMixin

# from . import db

class Futbrdata(db.Model, SerializerMixin):
    ano = db.Column(db.Integer, primary_key=True)
    vencedor = db.Column(db.String(250))
    vice = db.Column(db.String(250))
    terceiro_colocado = db.Column(db.String(250))
    quarto_colocado = db.Column(db.String(250))
    artilheiros = db.Column(db.String(250))
    gols = db.Column(db.Integer)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))


# from . import db

class URL(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)

    # def __repr__(self):
    #     return f"URL('{self.url}')"
