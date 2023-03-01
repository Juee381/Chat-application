from flask_restful import Resource, request
from flask import render_template, make_response
from flask_login import current_user, login_user
from model.user import get_user


class Login(Resource):
    @classmethod
    def get(cls):
        print("1")
        if current_user.is_authenticated:
            print("2")
            return make_response(render_template('home.html'))
        return make_response(render_template('login.html'))

    @classmethod
    def post(cls):
        username = request.form.get('username')
        password_input = request.form.get('password')
        user = get_user(username)

        if user and user.check_password(password_input):
            login_user(user)
            return make_response(render_template('home.html', username=username))

        return make_response(render_template('login.html', message="user not exists"))
