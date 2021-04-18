from helpers.verify_data import verify_data
from flask import jsonify
from models.artist import Artist
from helpers.truncate_id import truncate_id
from base64 import b64encode


def get_artists():
    artists = [artist.json() for artist in Artist.query.all()]
    return jsonify(artists), 200


def get_artist(artist_id):
    artist = Artist.query.filter_by(id=artist_id).first()
    if artist is None:
        return jsonify({'message': 'artista no encontrado'}), 404
    return jsonify(artist.json()), 200


def create_artist(request, base_url):
    if not verify_data(request=request):
        return jsonify({'message': 'input inválido'}), 400
    json = request.get_json(force=True)
    if json.get('name') is None or json.get('age') is None:
        return jsonify({'message': 'input inválido'}), 400
    artist_id = b64encode(json['name'].encode()).decode('utf-8')
    artist_id = truncate_id(artist_id)
    possible_artist = Artist.query.filter_by(id=artist_id).first()
    if possible_artist is None:
        artist = Artist.create(
            artist_id=artist_id, name=json['name'], age=json['age'], base_url=base_url)
        return jsonify(artist.json()), 201
    return jsonify({'message': 'artista ya existe'}), 409


def delete_artist(artist_id):
    artist = Artist.query.filter_by(id=artist_id).first()
    if artist is None:
        return jsonify({'message': 'artista inexistente'}), 404
    artist.delete()
    return jsonify({'message': 'artista eliminado'})
