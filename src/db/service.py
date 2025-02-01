from pymongo.database import Database


class Service:

    def __init__(self, db: Database):
        self.collection = db['service']

    def add_welcome_text(self, text: str):
        doc = {
            "welcome_text": True,
            "text": text
        }

        self.collection.insert_one(doc)

    def get_welcome_text(self) -> str | None:
        doc = self.collection.find_one({'welcome_text': True})
        return doc['text'] if doc else None
