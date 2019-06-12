from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

# neo4j的节点
# neo4j ogm

class User(GraphObject):
    __primarykey__ = "name"
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
