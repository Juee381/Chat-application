from db import chat_db

room_member_collection = chat_db.get_collection('room_members')


def create_room_member(room_name: str, username: str):
    room_member_collection.insert_one({'_id': {'room_name': room_name, 'username': username}})
