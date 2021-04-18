from models.album import Album
from models.artist import Artist
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from models.index import db


class Track(db.Model):
    __tablename__ = 'track'
    id = db.Column(db.String(22), primary_key=True)
    album_id = db.Column(db.String(22), db.ForeignKey('album.id'),
                         nullable=False)
    name = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    times_played = db.Column(db.Integer, nullable=False, default=0)
    url = db.Column(db.String(100), nullable=False)

    @classmethod
    def create(cls, track_id, album_id, name, duration, base_url):
        url = base_url + f'/albums/{album_id}'
        track = Track(id=track_id, album_id=album_id,
                      name=name, duration=duration, url=url)
        return track.save()

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
        album = Album.query.filter_by(id=self.album_id).first()
        artist = Artist.query.filter_by(id=album.artist_id).first()
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'artist': artist.name,
            'artist_id': artist.id,
            'album': album.name,
            'album_id': self.album_id,
            'times_played': self.times_played,
            'url': self.url,
        }
