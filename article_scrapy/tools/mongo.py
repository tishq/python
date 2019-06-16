import pymongo
class MongoPipeline(object):
    # 连接mongodb
    client = pymongo.MongoClient('localhost')
    db = client['csdn_test']
    collection = db['scrapy_items']
    # documents = collection.find()
    collection.insert_one(dict(item))
