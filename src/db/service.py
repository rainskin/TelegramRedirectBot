from pymongo.database import Database


class Service:

    def __init__(self, db: Database):
        self.collection = db['service']
        self.welcome_text = "✅"
        self.add_welcome_text()
        self.set_up_user_registration()

    def add_welcome_text(self):
        doc = self.collection.find_one({'welcome_text': True})
        if doc:
            return

        doc = {
            "welcome_text": True,
            "text": self.welcome_text
        }

        self.collection.insert_one(doc)

    def get_welcome_text(self) -> str | None:
        doc = self.collection.find_one({'welcome_text': True})
        return doc['text'] if doc else None

    def is_user_registration_enabled(self) -> bool | None:
        # need create this doc in the database manually

        doc = self.collection.find_one({'main_settings': True})
        return doc['enable_user_registration'] if doc else None

    def set_up_user_registration(self):
        doc = self.collection.find_one({'main_settings': True})

        if doc:
            return

        self.collection.insert_one({
            'main_settings': True,
            'enable_user_registration': True
        })
