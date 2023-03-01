from flask import Response, request, make_response, render_template
from flask_login import login_required, current_user

from model.room import get_room


class ViewRoom(Response):
    @classmethod
    @login_required
    def get(cls):
        room_name = request.form.get("room_name")
        room = get_room(room_name)

        if room:
            return make_response(
                render_template('view_room.html', room_name=room['_id'], username=current_user.username))

        return make_response(render_template('join_room.html', message="{} room does not exists".format(room)))
