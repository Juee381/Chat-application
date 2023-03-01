from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from flask_socketio import SocketIO, join_room

from resources.signup import SignUp
from resources.login import Login
from resources.logout import LogOut
from resources.create_room import Create_room
from resources.join_room import Join_room
from resources.room import ViewRoom
from model.user import get_user


app = Flask(__name__)
app.secret_key = "secret key"
api = Api(app)

socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)

api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
api.add_resource(LogOut, '/logout')
api.add_resource(Create_room, '/create_room')
api.add_resource(Join_room, '/join_room')
# api.add_resource(ViewRoom, '/room')
api.add_resource(ViewRoom, '/rooms', endpoint="room")


@login_manager.user_loader
def load_user(username):
    return get_user(username)


@socketio.on('join_room')
def handle_join_room_event(data):
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
