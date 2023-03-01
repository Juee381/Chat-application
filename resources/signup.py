from flask_restful import Resource, request
from flask import render_template, make_response

from pymongo.errors import DuplicateKeyError

from model.user import save_user


class SignUp(Resource):
    @classmethod
    def get(cls):
        return make_response(render_template('signup.html'))

    @classmethod
    def post(cls):
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            if username and email and password:
                print("1")
                save_user(username, email, password)
                print("2")
                return make_response(render_template('login.html', message="user created"))
            else:
                return make_response(render_template('signup.html', message="invalid input"))

        except DuplicateKeyError:
            return make_response(render_template('signup.html', message="user already exists"))

        except Exception as err:
            print(err)
