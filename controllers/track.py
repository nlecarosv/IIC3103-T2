from models.track import Track
from flask import jsonify
from helpers.truncate_id import truncate_id
from models.artist import Artist
from models.album import Album
from base64 import b64encode


def get_tracks():
    tracks = [track.json() for track in Track.query.all()]
    return jsonify(tracks), 200


def get_tracks_for_album(album_id):
    possible_album = Album.query.filter_by(id=album_id).first()
    if possible_album is None:
        return jsonify({'message': 'álbum no encontrado'}), 404
    album = possible_album
    tracks = [track.json() for track in album.tracks]
    return jsonify(tracks), 200


def get_tracks_for_artist(artist_id):
    print("Bien")
    possible_artist = Artist.query.filter_by(id=artist_id).first()
    if possible_artist is None:
        return jsonify({'message': 'artista no encontrado'}), 404
    artist = possible_artist
    albums = artist.albums
    tracks = []
    for album in albums:
        for track in album.tracks:
            tracks.append(track.json())
    return jsonify(tracks), 200


def get_track(track_id):
    track = Track.query.filter_by(id=track_id).first()
    if track is None:
        return jsonify({'message': 'Canción no encontrada'}), 404
    return jsonify(track.json()), 200


def create_track(album_id, request, base_url):
    print(album_id, 'albun_id')
    if len(album_id) == 0:
        return jsonify({'message': 'input inválido'}), 400
    possible_album = Album.query.filter_by(id=album_id).first()
    if possible_album is None:
        return jsonify({'message': 'álbum no existe'}), 422
    album = possible_album
    json = request.get_json(force=True)
    if json.get('name') is None or json.get('duration') is None:
        return jsonify({'message': 'input inválido'}), 400
    track_name = json['name']
    track_id = b64encode(
        f'{track_name}:{album.name}'.encode()).decode('utf-8')
    track_id = truncate_id(track_id)
    possible_track = Track.query.filter_by(id=track_id).first()
    if possible_track is None:
        track = Track.create(track_id=track_id, album_id=album_id,
                             name=json['name'], duration=json['duration'], base_url=base_url)
        return jsonify(track.json()), 201
    return jsonify({'message': 'canción ya existe'}), 409
