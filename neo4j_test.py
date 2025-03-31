from py2neo import Graph,Subgraph
from py2neo import Node,Relationship,Path

# 连接数据库
graph = Graph('bolt://localhost:7687', auth=('neo4j', '12345678'))

graph.delete_all()