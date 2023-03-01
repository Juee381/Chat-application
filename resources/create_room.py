from flask import make_response, render_template, request, url_for, redirect
from flask_login import login_required, current_user
from flask_restful import Resource

from pymongo.errors import DuplicateKeyError

from model.room import create_room


class Create_room(Resource):
    @classmethod
    @login_required
    def get(cls):
        return make_response(render_template('create_room.html'))

    @classmethod
    @login_required
    def post(cls):
        room_name = request.form.get('room_name')
        try:
            create_room(room_name, current_user.username)
            return redirect(url_for('room', room_name=room_name))

        except DuplicateKeyError:
            return make_response(
                render_template('create_room.html', message="{} room already exists".format(room_name)))
