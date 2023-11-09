import numpy as np

#import file
FILENAME = 'test_graph.txt'
file = open(FILENAME)

#get number of nodes, create adjacency matrix
file.seek(0)
nodes = int(file.readline())
graph = np.zeros((nodes, nodes), dtype = bool)

#populate adjacency matrix
l = file.readlines()
for line in l:
    graph[int(line.split()[0]) - 1][int(line.split()[1]) - 1] = True
print(graph)