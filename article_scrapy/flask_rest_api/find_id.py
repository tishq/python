# 连接mongodb
import pymongo
# flask restfull
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

client = pymongo.MongoClient('localhost')
db = client['csdn_test']
collection = db['scrapy_items']


class FindArticle(Resource):
    def get(self,ids):
        print(type(ids))
        articles = []
        article = {}
        # b= "1 3"
        # b= b.split()
        # print(b)
        # for j in b:
        #     print(type(j))
        #     j = int(j)
        #     print(type(j))
        #     print(j)
        ids = ids.split()
        for j in ids:
            print(type(j))
            j = int(j)
            ar = collection.find_one({'articleId': j})
            article['articleId'] = ar['articleId']
            article['title'] = ar['title']
            article['summary'] = ar['summary']
            article['author'] = ar['author']
            article['tag'] = ar['tag']
            article['url'] = ar['url']
            article['date'] = ar['date']
            article['star'] = ar['star']
            article['score'] = ar['score']
            article['views'] = ar['views']
            article['comments'] = ar['comments']
            article['source'] = ar['source']
            articles.append(article.copy())
            # articleId title summary author tag url date star score views comments source
        return articles



app = Flask(__name__)
api = Api(app)

api.add_resource(FindArticle, '/articles/<ids>')

if __name__ == '__main__':
    app.run(
        # python es_rest.py 可以看到效果(生产环境)
        host= '0.0.0.0',
        port= 5004,
        debug=True
    )
