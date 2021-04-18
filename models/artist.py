from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from models.index import db


class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.String(22), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(100), nullable=False)
    albums = db.relationship("Album", backref='artist',
                             lazy=True, cascade='all, delete-orphan')

    @classmethod
    def create(cls, artist_id, name, age, base_url):
        age = int(age)
        url = base_url + f'/artists/{artist_id}'
        artist = Artist(id=artist_id, name=name, age=age, url=url)
        return artist.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'url': self.url,
        }
