# py2neo测试 v4版本
# http://localhost:7474/browser/
from py2neo import *
graph = Graph("http://localhost:7474",username="neo4j",password="Yn971022")

node0 = Node('persion',name='aa')
node1 = Node('persion',name='bb')
node0['age'] = 10
node1['age'] = 20
# graph.create(node0)
# graph.create(node1)

# aa like bb
node0_like_node2 = Relationship(node0,'like',node1)
# graph.create(node0_like_node2)

# match
matcher = NodeMatcher(graph)
aa = matcher.match('persion').limit(10)
print(aa)
