# flask restfull
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource



import random
from collections import Counter

from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
import pymongo



# 连接graph
graph = Graph("http://localhost:7474",username="neo4j",password="Yn971022")

# match
matcher = NodeMatcher(graph)

# neo4j的节点
# neo4j ogm

# 用户节点 ogm
class User(GraphObject):
    __primarykey__ = "userId"
    userId = Property()
    name = Property()
    # (a-to-b <=> a->b )
    like = RelatedTo("Article","LIKE")

# 文章节点 ogm
class Article(GraphObject):
    __primarykey__ = "articleId"
    articleId = Property()
    title = Property()
    summary = Property()
    author = Property()
    tag = Property()
    url = Property()
    date = Property()
    star = Property()
    score = Property()
    views = Property()
    comments = Property()
    source = Property()
    # (a-from-b <=> b->a )
    like = RelatedFrom("User", "LIKE")



app = Flask(__name__)
api = Api(app)

class UAR(Resource):
    def get(self,userId,articleId):
        print(type(userId))
        uId = int(userId)
        print(type(uId))
        aId = int(articleId)

        u = User.match(graph).where(userId=uId).first()
        a = Article.match(graph).where(articleId=1).first()
        print(u)
        print(a)
        u.like.add(a)
        graph.push(u)
        return userId+"like"+articleId

api.add_resource(UAR, '/kgr/<userId>/<articleId>')

if __name__ == '__main__':
    app.run(
        # python es_rest.py 可以看到效果(生产环境)
        host= '0.0.0.0',
        port= 5003,
        debug=True
    )
