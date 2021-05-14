from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *
from pyspark.sql.functions import *
import pyspark.sql.functions as F

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_shortest_distances(graphframe, dst_id):
    
    # Find shortest distances in the given graphframe to the vertex which has id `dst_id`
    # The result is a dictionary where key is a vertex id and the corresponding value is
    # the distance of this node to vertex `dst_id`.
    df = graphframe.shortestPaths(landmarks=[dst_id])
    #df.show()

    g2 = df.withColumn('distances', F.map_values('distances'))
    g2 = g2.collect()
    #print(g2)

    dic = {}
    for i in g2:
        dic[i[0]] = i[1]
    #print(dic)
    #print(type(dic['1']))

    dic2 = {}
    for k, v in dic.items():
        if len(v) > 0:
            dic2[k] = v[0]
        else:
            dic2[k] = -1
    #print(dic2)
    res = {k: v for k, v in sorted(dic2.items(), key=lambda x: int(x[0]))}
    
    return res

if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:
        for line in f:
            line = line.strip()
            line = line.split(' ')
            src = line[0]
            # TODO: Parse line to get ids of vertices that src is connected to
            dst_list = line[1:]
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list, ['id'])  # TODO: Create dataframe for vertices
    edges = spark.createDataFrame(edge_list, ['src', 'dst'])  # TODO: Create dataframe for edges

    #vertices.show()
    #edges.show()

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/shortest-paths")
    
    # We want the shortest distance from every vertex to vertex 1
    #get_shortest_distances(g, '1')
    for k, v in get_shortest_distances(g, '1').items():
       print(k, v)
