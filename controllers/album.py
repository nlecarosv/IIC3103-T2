from helpers.verify_data import verify_data
from flask import jsonify
from helpers.truncate_id import truncate_id
from models.artist import Artist
from models.album import Album
from base64 import b64encode


def get_albums():
    albums = [album.json() for album in Album.query.all()]
    return jsonify(albums), 200


def get_albums_for_artist(artist_id):
    possible_artist = Artist.query.filter_by(id=artist_id).first()
    if possible_artist is None:
        return jsonify({'message': 'artista no encontrado'}), 404
    artist = possible_artist
    albums = [album.json() for album in artist.albums]
    return jsonify(albums), 200


def get_album(album_id):
    album = Album.query.filter_by(id=album_id).first()
    if album is None:
        return jsonify({'message': 'álbum no encontrado'}), 404
    return jsonify(album.json()), 200


def create_album(artist_id, request, base_url):
    if not verify_data(request=request):
        return jsonify({'message': 'input inválido'}), 400
    if len(artist_id) == 0:
        return jsonify({'message': 'input inválido'}), 400
    possible_artist = Artist.query.filter_by(id=artist_id).first()
    if possible_artist is None:
        return jsonify({'message': 'artista no existe'}), 422
    artist = possible_artist
    json = request.get_json(force=True)
    if json.get('name') is None or json.get('genre') is None:
        return jsonify({'message': 'input inválido'}), 400
    album_name = json['name']
    album_id = b64encode(
        f'{album_name}:{artist.name}'.encode()).decode('utf-8')
    album_id = truncate_id(album_id)
    possible_album = Album.query.filter_by(id=album_id).first()
    if possible_album is None:
        album = Album.create(album_id=album_id, artist_id=artist_id,
                             name=json['name'], genre=json['genre'], base_url=base_url)
        return jsonify(album.json()), 201
    return jsonify({'message': 'álbum ya existe'}), 409


def delete_album(album_id):
    album = Album.query.filter_by(id=album_id).first()
    if album is None:
        return jsonify({'message': 'álbum no encontrado'}), 404
    album.delete()
    return jsonify({'message': 'álbum eliminado'})
