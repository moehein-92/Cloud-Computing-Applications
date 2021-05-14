import json
import boto3

def graph_dict(string):
    s = string.split(',')
    graph = {}
    for edge in s:
        edge = edge.split('->')
        graph.setdefault(edge[0], []).append(edge[1])
    return graph

def bfs(graph, vertex):
    queue = deque([vertex])
    level = {vertex: 0}
    while queue:
        v = queue.popleft()
        if v in graph:
            for n in graph[v]:
                if n not in level:
                    queue.append(n)
                    level[n] = level[v] + 1
    return level

def find_distances(graph):
    city_dist = {}
    for city in graph:
        distances = bfs(graph, city)
        for dest_city, dest_dist in distances.items():
            if (dest_city != city) and (city, dest_city) not in city_dist:
                city_dist[(city, dest_city)] = dest_dist
    return city_dist

def lambda_handler(event, context): 
    dynamoDB = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    cityTable = dynamoDB.Table('Cities')
    s = event['graph']
    graph = graph_dict(s)
    city_dist = find_distances(graph)

    for pair, dist in city_dist.items():
        cityTable.put_item(
            Item={
                'source' : pair[0],
                'destination': pair[1],
                'distance' : dist
            }
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful Insert')
    }
