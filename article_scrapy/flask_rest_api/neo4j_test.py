# py2neo测试 v4版本
# http://localhost:7474/browser/
import neo as neo
from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

graph = Graph("http://localhost:7474",username="neo4j",password="Yn971022")

node0 = Node('persion',name='aa')
node1 = Node('persion',name='bb')
node2 = Node('persion',name='cc')
node3 = Node('persion',name='dd')
node0['age'] = 10
node1['age'] = 20
# graph.create(node0)
# graph.create(node1)

# aa like bb
node0_like_node2 = Relationship(node0,'like',node1)
# graph.create(node0_like_node2)

# match
matcher = NodeMatcher(graph)

aa = matcher.match('persion', age=20).first()
print(aa)

# 依据节点属性来检索
# aa = matcher.match('persion')
# print(list(aa.where("_.name =~ 'a.*'")))

# 依据关系来检索
# v4一个特性

##############################################################
#  ogm (object graph mapping)


class Movie(GraphObject):
    __primarykey__ = "title"

    title = Property()
    tag_line = Property("tagline")
    released = Property()
    # (a-from-b <=> b->a )
    actors = RelatedFrom("Person", "ACTED_IN")
    directors = RelatedFrom("Person", "DIRECTED")
    producers = RelatedFrom("Person", "PRODUCED")


class Person(GraphObject):
    __primarykey__ = "name"

    name = Property()
    born = Property()
    # (a-to-b <=> a->b )
    acted_in = RelatedTo(Movie)
    directed = RelatedTo(Movie)
    produced = RelatedTo(Movie)


p1 = Person()
p1.name = 'p1'
graph.push(p1)

p2 = Person()
p2.name = "p2"
p2.born = "2019-01-01"
graph.push(p2)

m1 = Movie()
m1.title = "m1"
m1.actors.add(p1)
graph.push(m1)


m2 = Movie()
m2.title = "m2"
graph.push(m2)
m2.actors.add(p2)
graph.push(m2)





