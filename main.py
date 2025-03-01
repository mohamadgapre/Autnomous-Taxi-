import pathFinding
import graph
import numpy as np
import math

path = pathFinding.dijkstra(graph.graph, 'Z', 'A')

for i in range(1, len(path)):
    #print(path[i])
    currX = graph.graph[path[i]]['coordinates']['x']
    currY = graph.graph[path[i]]['coordinates']['y']

    prevX = graph.graph[path[i-1]]['coordinates']['x']
    prevY = graph.graph[path[i-1]]['coordinates']['y']

    #current_direction_x =
    #current_direction_y =

    #desired_direction_x =
    #desired_direction_y =

    #cross_product = prevX*currY - currX*prevY
    #print(cross_product)
    #print(graph.graph[path[i]]['coordinates']['x'])
    #print(graph.graph[path[i]]['coordinates']['y'])

def findClosest(graph, x, y):
    currMin = float("inf")
    closest = 'Not Found'
    for node in graph:
        vertex_x = graph[node]['coordinates']['x']
        vertex_y = graph[node]['coordinates']['y']
        dist = math.sqrt((x - vertex_x) ** 2 + (y - vertex_y) ** 2)
        if dist < currMin:
            currMin = dist
            closest = node
    return closest

while(1):
    print("getting fare")
    #call vpfs, save fare info in 'fare' (placeholder values now)
    destination_x = 175
    destination_y = 459
    print("destination (x,y): " + str(destination_x) + "," + str(destination_y))
    source_x = 305
    source_y = 29
    print("Source (x,y): " + str(source_x) + "," + str(source_y))

    # Find closest vertex to source
    closest_source_vertex = findClosest(graph.graph, source_x, source_y)
    print("Closest source vertex: " + closest_source_vertex)
    path_to_source = pathFinding.dijkstra(graph.graph, 'M', closest_source_vertex)
    # then do linefollowing / turning algorithm according to this path
    print("Moving to source")
    for i in range(1, len(path_to_source)):
        print(path_to_source[i])

    # Find closest vertex to destination
    closest_dest_vertex = findClosest(graph.graph, destination_x, destination_y)
    print("Closest destination vertex: " + closest_dest_vertex)
    path_to_dest = pathFinding.dijkstra(graph.graph, closest_source_vertex, closest_dest_vertex)
    # then do linefollowing / turning algorithm according to this path
    print("Moving to destination")
    for i in range(1, len(path_to_dest)):
        print(path_to_dest[i])

    break