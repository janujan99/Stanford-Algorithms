import random
import numpy as np


def shortest_path(vertices, edge_weights):
    X = set([1])
    A = {1: 0}
    while len(X) < len(vertices):
        # pick a vertex (v,w) in edge_weights with v in X, and w not in X
        min_vertex = None
        lowest_weight = np.inf
        for edge in edge_weights:
            if edge[0] in X and not edge[1] in X:
                greedy_criterion = A[edge[0]] + edge_weights[edge]
                if greedy_criterion < lowest_weight:
                    lowest_weight = greedy_criterion
                    min_vertex = edge
        X.add(min_vertex[1])
        A[min_vertex[1]] = lowest_weight
    return A


#adj_list = {"s": ["v", "w"], "v": ["w", "t"], "w": ["t"], "t": []}
#edge_weights = {("s", "v"): 1, ("s", "w"): 4, ("v", "w")                : 2, ("v", "t"): 7, ("w", "t"): 3}
lines = open("dijkstraData.txt", "r").readlines()
vertices = set()
edge_weights = {}
for line in lines:
    arr = line.split("\t")
    vertex = int(arr[0])
    vertices.add(vertex)
    for edge in arr[1:-1]:
        comma_index = edge.find(",")
        connecting_vertex = int(edge[:comma_index])
        weight = int(edge[comma_index+1:])
        edge_weights[(vertex, connecting_vertex)] = weight

result = shortest_path(vertices, edge_weights)

print(result)
