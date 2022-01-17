import pandas as pd
import threading
import sys


def dfs_loop(graph, length):
    global t
    global s
    global leader
    global finishing_times
    t = 0
    s = None
    leader = [None]*length
    finishing_times = [None]*length

    visited = set()
    print("First pass: ")
    # first pass, traversing graph in reverse order
    for i in range(length, 0, -1):
        if i in graph and not i in visited:
            s = i
            dfs(graph, i, visited, rev=True)

    # construct graph with finishing time
    finishing_times_graph = {}
    for node in graph:
        finishing_times_graph[finishing_times[node-1]
                              ] = [finishing_times[x-1] for x in graph[node]]

    # second pass, traversing graph with finishing times in normal order
    print("Second pass: ")
    visited = set()
    for i in range(len(finishing_times_graph), 0, -1):
        if i in graph and not i in visited:
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
        print(i)
        finishing_times[i-1] = t

    return


directed_graph = {1: [4], 2: [8], 3: [6], 4: [7],
            5: [2], 6: [9], 7: [1], 8: [5, 6], 9: [3, 7]}

assignment_graph = {}
max_node = 0
threading.stack_size(67108864)
sys.setrecursionlimit(2**20)
thread = threading.Thread(target=dfs)
thread.start()
lines = open("SCC.txt", "r").readlines()
for line in lines:
    split = [int(i) for i in line.split(" ")[:-1]]
    vertex = split[0]
    if vertex in assignment_graph:
        assignment_graph[vertex].append(int(split[1]))
    else:
        assignment_graph[vertex] = [split[1]]
    
    if vertex > max_node:
        max_node = vertex

print("Max node: " + str(vertex))
dfs_loop(assignment_graph, max_node)
df = pd.DataFrame()
df["Leaders"] = leader
df.to_csv(path_or_buf='./leaders.csv', index=False)
#print("Finishing times: " + str(finishing_times))
#print("Leaders: " + str(leader))
#print("Sizes: ")
