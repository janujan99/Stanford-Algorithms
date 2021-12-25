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
        # whichever node has label with smaller value, keep that one during the contraction and discard node with higher label value later
        contraction_lst.append((a, b))
        kept_vertex = min([a, b])
        removed_vertex = max([a, b])

        # add all edges from removed_vertex's edge list to kept_vertex's edge list, with the exception of the removed vertex (avoid adding self loops)
        arr = [x for x in graph[kept_vertex] if x != removed_vertex]
        arr.extend([v for v in graph[removed_vertex] if v != kept_vertex])

        graph[kept_vertex] = [y for y in arr]

        # remove the removed_vertex from all other edge lists
        for node in graph:
            graph[node] = [x for x in graph[node] if x != removed_vertex]

        # remove the removed_vertex from graph
        del graph[removed_vertex]

    return max([len(graph[list(graph.keys())[0]]), len(graph[list(graph.keys())[1]])])


contr_list = []
adj_list = {1: [2, 3, 4], 2: [1, 4], 3: [1, 4, 5], 4: [1, 2, 3], 5: [3]}
print("Min cut: " + str(min_cut(adj_list, contr_list)))
print("Graph: " + str(adj_list))
print("Cut order: " + str(contr_list))
