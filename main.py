
from flask import Flask
from flask import request
from config import config
from models.index import db
import controllers.artist as artist_controller
import controllers.album as album_controller
import controllers.track as track_controller


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        return app


enviroment = config['development']
base_url = enviroment.BASE_URL
app = create_app(enviroment)


# artist
@app.route('/artists', methods=['GET'])
def get_artists():
    return artist_controller.get_artists()


@app.route('/artists/<id>', methods=['GET'])
def get_artist(id):
    return artist_controller.get_artist(artist_id=id)


@app.route('/artists', methods=['POST'])
def create_artist():
    return artist_controller.create_artist(request=request, base_url=base_url)

# @app.route('/api/v1/users/<id>', methods=['DELETE'])
# def delete_user(id):
#   user = User.query.filter_by(id=id).first()
#   if user is None:
#     return jsonify({'message': 'User does not exists'}), 404
#   user.delete()
#   return jsonify({'user': user.json() })

# @app.route('/api/v1/users/<id>', methods=['PUT'])
# def update_user(id):
#   user = User.query.filter_by(id=id).first()
#   if user is None:
#     return jsonify({'message': 'User does not exists'}), 404
#   json = request.get_json(force=True)
#   if json.get('username') is None:
#     return jsonify({'message': 'Bad request'}), 400
#   user.username = json['username']
#   user.update()
#   return jsonify({'user': user.json() })


# albums
@app.route('/albums', methods=['GET'])
def get_albums():
    return album_controller.get_albums()


@app.route('/artists/<id>/albums', methods=['GET'])
def get_albums_for_artist(id):
    return album_controller.get_albums_for_artist(artist_id=id)


@app.route('/albums/<id>', methods=['GET'])
def get_album(id):
    return album_controller.get_album(album_id=id)


@app.route('/artists/<artist_id>/albums', methods=['POST'])
def create_album(artist_id):
    return album_controller.create_album(artist_id=artist_id, request=request, base_url=base_url)


# tracks
@app.route('/tracks', methods=['GET'])
def get_tracks():
    return track_controller.get_tracks()


@app.route('/albums/<id>/tracks', methods=['GET'])
def get_tracks_for_album(id):
    return track_controller.get_tracks_for_album(album_id=id)


@app.route('/artists/<id>/tracks', methods=['GET'])
def get_tracks_for_artist(id):
    return track_controller.get_tracks_for_artist(artist_id=id)


@app.route('/tracks/<id>', methods=['GET'])
def get_track(id):
    return track_controller.get_track(track_id=id)


@app.route('/albums/<album_id>/tracks', methods=['POST'])
def create_track(album_id):
    return track_controller.create_track(album_id=album_id, request=request, base_url=base_url)


if __name__ == '__main__':
    app.run(debug=True)
