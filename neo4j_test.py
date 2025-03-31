from py2neo import Graph,Subgraph
from py2neo import Node,Relationship,Path

# 连接数据库
graph = Graph('bolt://localhost:7687', auth=('neo4j', '123456'))

graph.delete_all()