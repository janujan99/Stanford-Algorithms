import random
import numpy as np

def min_cut(graph, contraction_lst):
    while len(graph) > 2:
        # pick two random vertices that have an edge
        a = 0
        b = 0
        valid_edge = False
        key_list = list(graph.keys())
        while not valid_edge:
            a = key_list[random.randint(0, len(graph)-1)]
            if len(graph[a]) > 0:
                b = graph[a][random.randint(0,len(graph[a])-1)]
                valid_edge = True

        # add edge to be contracted to contraction_lst
        contraction_lst.append((a, b))

        # whichever node has label with smaller value, keep that one during the contraction and discard node with higher label value later
        kept_vertex = min([a, b])
        removed_vertex = max([a, b])

        # add all edges from removed_vertex's edge list to kept_vertex's edge list, with the exception of the removed vertex (avoid adding self loops)
        arr = [x for x in graph[kept_vertex] if x != kept_vertex]
        arr.extend([v for v in graph[removed_vertex] if v != kept_vertex])

        graph[kept_vertex] = [y for y in arr]

        # replace the removed_vertex from all other edge lists with kept_vertex, unless the iteration is on the kept_vertex itself
        for node in graph:
            if node == kept_vertex:
                graph[node] = [x for x in graph[node] if x != removed_vertex]
            else:
                arr = []
                for x in graph[node]:
                    if x == removed_vertex:
                        arr.append(kept_vertex)
                    else:
                        arr.append(x)
                graph[node] = arr
        # remove the removed_vertex from graph
        del graph[removed_vertex]
    return len(graph[list(graph.keys())[0]])

graph = {}
lines = open("kargerMinCut.txt", "r").readlines()

for line in lines:
    split = [int(x) for x in line.split("\t")[:-1]]
    graph[split[0]] = split[1:]

contr_list = []
minCut = np.inf
#adj_list = {1: [2,3,4,5], 2: [1,3,4,5], 3: [1,2,4,5,7], 4: [1,2,3,5,8], 5: [1,2,3,4,6], 6: [5,7,8,9,10], 7: [3,6,8,9,10], 8: [4,6,7,9,10], 9: [6,7,8,10], 10:[6,7,8,9]}
for x in range(100):
    adj_list = {}
    for node in graph:
        adj_list[node] = [x for x in graph[node]]
    res = min_cut(adj_list, [])
    if res < minCut:
        minCut = res
print(minCut)
#print("Graph: " + str(adj_list))
#print("Cut order: " + str(contr_list))
