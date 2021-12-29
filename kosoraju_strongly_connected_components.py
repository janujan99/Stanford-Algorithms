def dfs_loop(graph):
    global t
    global s
    global leader
    global finishing_times
    t = 0
    s = None
    leader = [None]*len(graph)
    finishing_times = [None]*len(graph)

    visited = set()
    # first pass, traversing graph in reverse order
    for i in range(len(graph), 0, -1):
        if not i in visited:
            s = i
            dfs(graph, i, visited, rev=True)

    # construct graph with finishing time
    finishing_times_graph = {}
    for node in graph:
        finishing_times_graph[finishing_times[node-1]
                              ] = [finishing_times[x-1] for x in graph[node]]

    # second pass, traversing graph with finishing times in normal order
    visited = set()
    for i in range(len(finishing_times_graph), 0, -1):
        if not i in visited:
            s = i
            dfs(finishing_times_graph, i, visited)

    return


def dfs(graph, i, visited, rev=False):
    visited.add(i)

    global s
    global t

    to_be_traversed = []

    if not rev:
        leader[i-1] = s
        to_be_traversed = [x for x in graph[i]]

    else:
        for node in graph:
            if i in graph[node]:
                to_be_traversed.append(node)

    for node in to_be_traversed:
        if not node in visited:
            dfs(graph, node, visited, rev)

    if rev:
        t += 1
        finishing_times[i-1] = t

    return


adj_list = {1: [4], 2: [8], 3: [6], 4: [7],
            5: [2], 6: [9], 7: [1], 8: [5, 6], 9: [3, 7]}

dfs_loop(adj_list)

print("Finishing times: " + str(finishing_times))
print("Leaders: " + str(leader))
print("Sizes: ")
