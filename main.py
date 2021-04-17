
from flask import Flask
from flask import request
from config import config
from models.index import db
import controllers.artist as artist_controller
import controllers.album as album_controller


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

# @app.route('/artists/<id>', methods=['GET'])
# def get_artist(id):
#   artist = Artist.query.filter_by(id=id).first()
#   if artist is None:
#     return jsonify({'message': 'artista no encontrado'}), 404
#   return jsonify(artist.json()), 200


@app.route('/artists/<artist_id>/albums', methods=['POST'])
def create_album(artist_id):
    return album_controller.create_album(artist_id=artist_id, request=request, base_url=base_url)

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


# @app.route('/api/v1/users/<id>', methods=['DELETE'])
# def delete_user(id):
#   user = User.query.filter_by(id=id).first()
#   if user is None:
#     return jsonify({'message': 'User does not exists'}), 404
#   user.delete()
#   return jsonify({'user': user.json() })
if __name__ == '__main__':
    app.run(debug=True)
