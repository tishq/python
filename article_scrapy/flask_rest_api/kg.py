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
class User(GraphObject):
    __primarykey__ = "userId"
    userId = Property()
    name = Property()
    # (a-to-b <=> a->b )
    like = RelatedTo("Article","LIKE")

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
# 建立文章用户知识图谱
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


# 建立文章用户知识图谱
for i in range(10):
    user = User()
    user.userId = i
    user.name = 'user' + str(i)

    # 每个用户随机喜欢十篇文章
    for j in range(10):
        # 生成一个1-100之间的随机整数
        r = random.randint(1, 150)
        print(r)
        user.like.add(Article.match(graph).where(articleId = r).first())
        graph.push(user)



def kgr(userId):
    # 推荐文章id列表
    articleId = []

    # 根据userId找到和该用户有喜欢文章交集的用户
    uu = graph.run("match p=(u1:User{userId:"+str(userId)+"})-[r1:LIKE]->(a1)<-[r2:LIKE]-(u2)-[r3:LIKE]->(a2) "
                   # "with u2, count(u2) as c " 
                   # "set u2.c=c "
                   # "ORDER BY u2.name DESC LIMIT 100 "
                   "return u2.userId").data()
    print(uu)

    # 拿到用户列表
    us = []
    for u in uu:
        us.append(u['u2.userId'])
    print(us)

    # 根据userId找到和该用户有喜欢文章交集数最多的用户
    um = Counter(us).most_common(1)[0][0]
    print(um)

    # 根据userId找到和该用户有喜欢文章交集数最多的用户喜欢的文章的articleId
    aa = graph.run("match p=(u1:User{userId:"+str(userId)+"})-[r1:LIKE]->(a1)<-[r2:LIKE]-(u2:User{userId:"+str(um)+"})-[r3:LIKE]->(a2) "                                                                                            
                   "with a2 " 
                   # "set u2.c=c "
                   "ORDER BY a2.articleId DESC LIMIT 100 "
                   "return DISTINCT a2.articleId").data()
    ra = []
    for a in aa:
        ra.append(a['a2.articleId'])
    print(ra)
    return ra

kgr(5)

