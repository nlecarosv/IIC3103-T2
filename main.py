
from flask import Flask
from flask import request, jsonify
from config import config
from models.index import db
import controllers.artist as artist_controller
import controllers.album as album_controller
import controllers.track as track_controller
import os


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        return app


enviroment = config[os.environ['ENVIRONMENT']]
base_url = enviroment.BASE_URL
app = create_app(enviroment)


@app.route('/artists', methods=['GET'])
def get_artists():
    return artist_controller.get_artists()


@app.route('/artists', methods=['POST'])
def create_artist():
    print('\n\n/artists', request.get_data())
    return artist_controller.create_artist(request=request, base_url=base_url)


@app.route('/artists/<id>', methods=['GET'])
def get_artist(id):
    return artist_controller.get_artist(artist_id=id)


@app.route('/artists/<id>', methods=['DELETE'])
def delete_artist(id):
    return artist_controller.delete_artist(artist_id=id)


@app.route('/artists/<id>/albums', methods=['GET'])
def get_albums_for_artist(id):
    return album_controller.get_albums_for_artist(artist_id=id)


@app.route('/artists/<artist_id>/albums', methods=['POST'])
def create_album(artist_id):
    print(f'\n\n/artists/{artist_id}/albums', request.get_data())
    return album_controller.create_album(artist_id=artist_id, request=request, base_url=base_url)


@app.route('/artists/<id>/albums/play', methods=['PUT'])
def play_tracks_from_artist(id):
    return track_controller.play_tracks_from_artist(artist_id=id)


@app.route('/artists/<id>/tracks', methods=['GET'])
def get_tracks_for_artist(id):
    return track_controller.get_tracks_for_artist(artist_id=id)


@app.route('/albums', methods=['GET'])
def get_albums():
    return album_controller.get_albums()


@app.route('/albums/<id>', methods=['GET'])
def get_album(id):
    return album_controller.get_album(album_id=id)


@app.route('/albums/<id>', methods=['DELETE'])
def delete_album(id):
    return album_controller.delete_album(album_id=id)


@app.route('/albums/<id>/tracks', methods=['GET'])
def get_tracks_for_album(id):
    return track_controller.get_tracks_for_album(album_id=id)


@app.route('/albums/<album_id>/tracks', methods=['POST'])
def create_track(album_id):
    print(f'\n\n/albums/{album_id}/tracks', request.get_data())
    return track_controller.create_track(album_id=album_id, request=request, base_url=base_url)


@app.route('/albums/<id>/tracks/play', methods=['PUT'])
def play_tracks_from_album(id):
    return track_controller.play_tracks_from_album(album_id=id)


@app.route('/tracks', methods=['GET'])
def get_tracks():
    return track_controller.get_tracks()


@app.route('/tracks/<id>', methods=['GET'])
def get_track(id):
    return track_controller.get_track(track_id=id)


@app.route('/tracks/<id>', methods=['DELETE'])
def delete_track(id):
    return track_controller.delete_track(track_id=id)


@app.route('/tracks/<id>/play', methods=['PUT'])
def play_track(id):
    return track_controller.play_track(track_id=id)


@app.route('/')
def welcome():
    return jsonify({'message': 'Bienvenido. Revisa https://app.swaggerhub.com/apis-docs/dedarritchon/Integracionify para más obtener más información.'}), 400


@app.route('/<path>')
def catch_inexisting_routes(path):
    return jsonify({'message': 'Ruta no válida. Revisa https://app.swaggerhub.com/apis-docs/dedarritchon/Integracionify para más información.'}), 400


if __name__ == '__main__':
    app.run()
