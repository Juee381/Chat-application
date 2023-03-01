from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:test@chatapp.nlsckxz.mongodb.net/?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
