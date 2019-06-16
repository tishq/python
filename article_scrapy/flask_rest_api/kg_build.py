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



# 连接mongodb
client = pymongo.MongoClient('localhost')
db = client['csdn_test']
collection = db['scrapy_items']
documents = collection.find()

# 遍历mongo集合
# 建立文章节点
for document in documents:
    print(document)

    article = Article()
    article.articleId=document['articleId']
    article.title = document['title']
    article.summary = document['summary']
    article.author = document['author']
    article.tag = document['tag']
    article.url = document['url']
    article.date = document['date']
    article.star = document['star']
    article.score = document['score']
    article.views = document['views']
    article.comments = document['comments']
    article.source = document['source']

    graph.push(article)
# articleId title summary author tag url date star score views comments source


# 建立用户节点
for i in range(100):
    user = User()
    user.userId = i
    user.name = 'user' + str(i)
    print(user)
    graph.push(user)

    # 每个用户随机喜欢十篇文章
    # for j in range(10):
    #     # 生成一个1-60000之间的随机整数
    #     r = random.randint(1, 100)
    #     print(r)
    #     user.like.add(Article.match(graph).where(articleId = r).first())
    #     graph.push(user)

