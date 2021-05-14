from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()

def get_connected_components(graphframe):
    result = graphframe.connectedComponents()
    d = dict()
    #print(result)
    for i in result.rdd.collect():
        #print(i)
        c = i['component']
        if c not in d:
            d[c] = list()
        d[c].append(str(i['id']))
    #print(d)
    return list(d.values())

if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:  # Do not modify
        for line in f:
            line = line.strip().split()
            src = line[0]  # TODO: Parse src from line
            dst_list = line[1:]  # TODO: Parse dst_list from line
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]


    vertices = spark.createDataFrame(vertex_list, ['id'])  # TODO: Create vertices dataframe
    edges = spark.createDataFrame(edge_list, ['src', 'dst'])  # TODO: Create edges dataframe

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/connected-components")

    result = get_connected_components(g)
    for line in result:
        print(' '.join(line))