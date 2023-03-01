from flask_restful import Resource
from flask_login import login_required, logout_user
from flask import make_response, render_template


class LogOut(Resource):
    @classmethod
    @login_required
    def get(cls):
        logout_user()
        return make_response(render_template('login.html'))
