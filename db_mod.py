import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['pyinance']
collection = db['stocks']

class DB_Mod:

    def __init__(self, input):
        self.obj = input

    def post(self):
        collection.insert_one(self.obj)

    # def delete(self):
    #     if collection.find_one(self.obj["id"]):
    #         collection.delete_one()
    # def update(self):
    #     pass
    # def get(self):
    #     pass
    # def find(self):
    #     pass
