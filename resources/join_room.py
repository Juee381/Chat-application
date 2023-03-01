from flask import make_response, render_template
from flask_restful import Resource
from flask_login import login_required


class Join_room(Resource):
    @classmethod
    @login_required
    def get(cls):
        return make_response(render_template('join_room.html'))
