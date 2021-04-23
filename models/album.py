from models.artist import Artist
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from models.index import db


class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.String(22), primary_key=True)
    artist_id = db.Column(db.String(22), db.ForeignKey('artist.id'),
                          nullable=False)
    name = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    tracks = db.relationship("Track", backref='album',
                             lazy=True, cascade='all, delete-orphan')

    @classmethod
    def create(cls, album_id, artist_id, name, genre, base_url):
        url = base_url + f'/albums/{album_id}'
        album = Album(id=album_id, artist_id=artist_id,
                      name=name, genre=genre, url=url)
        return album.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def json(self):
        artist = Artist.query.filter_by(id=self.artist_id).first()
        return {
            'id': self.id,
            'artist_id': self.artist_id,
            'name': self.name,
            'genre': self.genre,
            'artist': artist.url,
            'tracks': f'{self.url}/tracks',
            'self': self.url,
        }
