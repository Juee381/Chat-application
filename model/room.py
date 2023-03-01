from db import chat_db
from model.room_member import create_room_member

room_collection = chat_db.get_collection('room')


def create_room(room_name: str, username: str) -> None:
    room_collection.insert_one({'_id': room_name})
    create_room_member(room_name, username)


def get_room(room_name: str):
    room_collection.find_one({'_id': room_name})
