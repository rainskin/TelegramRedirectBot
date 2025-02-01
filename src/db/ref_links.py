from pymongo.database import Database


class RefLinks:

    def __init__(self, db: Database):
        self.collection = db['ref links']

    def register_or_create_tag(self, tag: str):
        doc = self.collection.find_one({"tag": tag})
        if doc:
            self.__register_tag(tag)
        else:
            self.__create_new_tag(tag)

    def __create_new_tag(self, tag):
        doc = {
            "tag": tag,
            'amount': 1,
            'comment': "",
        }

        self.collection.insert_one(doc)

    def __register_tag(self, tag: str):
        self.collection.update_one({"tag": tag}, {"$inc": {"amount": 1}})
