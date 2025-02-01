from datetime import datetime

from pymongo.database import Database

from loader import db


class Users:

    def __init__(self, db: Database):
        self.collection = db['users']

    def add(self, full_name: str, username: str, user_id: int):
        doc = {
            'full_name': full_name,
            'username': username,
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.collection.insert_one(doc)

    def is_new(self, user_id: int) -> bool:
        doc = self.collection.find_one({'user_id': user_id})
        return not bool(doc)
