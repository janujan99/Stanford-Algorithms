import random


def min_cut(graph, contraction_lst):
    while len(graph) > 2:
        # pick two random vertices that have an edge
        a = 0
        b = 0
        valid_edge = False
        key_list = list(graph.keys())
        while not valid_edge:
            a = key_list[random.randint(0, len(graph)-1)]
            b = key_list[random.randint(0, len(graph)-1)]
            if a != b and a in graph[b]:
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
    print(len(graph[list(graph.keys())[0]]) == len(graph[list(graph.keys())[1]]))
    return len(graph[list(graph.keys())[0]])

graph = {}
lines = open("kargerMinCut.txt", "r").readlines()

for line in lines:
    split = [int(x) for x in line.split("\t")[:-1]]
    graph[split[0]] = split[1:]


for x in range(100000):
    print("Min cut: " + str(min_cut(graph, [])))
#print("Graph: " + str(graph))
#print("Cut order: " + str(contr_list))
