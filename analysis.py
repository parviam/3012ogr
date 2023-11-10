from collections import defaultdict

#create a Graph class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):    #basic data structure functions
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def is_valid_next_edge(self, u, v): 
        if len(self.graph[u]) == 1:
            return True
        else:
            visited = [False] * (self.V)
            count1 = self.dfs_count(u, visited)

            self.remove_edge(u, v)
            visited = [False] * (self.V)
            count2 = self.dfs_count(u, visited)

            self.add_edge(u, v)

            return False if count1 > count2 else True

    def dfs_count(self, v, visited):
        count = 1
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                count = count + self.dfs_count(i, visited)

        return count

    def is_eulerian_circuit(self):      #all non-zero degree vertices connected?
        if not self.is_connected():
            return False

        odd = 0
        for i in range(self.V):                 #count odd vertices - must be even number!
            if len(self.graph[i]) % 2 != 0:
                odd += 1
        if odd != 0 and odd != 2:
            return False

        return (odd == 0) or (odd == 2 and self.is_connected())     #check connected if odd ct. 2

    def is_connected(self):
        visited = [False] * (self.V)        #init matrix - all vetices unvisited

        for i in range(self.V):             #get first vertex with degree >0, return false if none found
            if len(self.graph[i]) > 1:
                break
        if i == self.V - 1:     #or if its the last one it fails anyway bc what's it connecting to?
            return True

        self.dfs(i, visited)        #depth-first search

        for i in range(self.V):         #was everything visited?
            if not visited[i] and len(self.graph[i]) > 0:
                return False

        return True
    def dfs(self, v, visited):      #recursive depth-first search
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)
    def is_hamiltonian(self):
        def hamiltonian_util(path, pos):
            if pos == V:
                return self.graph[path[pos - 1]][path[0]] == 1       #vertex between these two points?

            for v in range(1, V):
                if is_valid(v, pos, path):
                    path[pos] = v

                    if hamiltonian_util(path, pos + 1):         #recursive: check every possible path
                        return True

                    path[pos] = -1

            return False

        def is_valid(v, pos, path):                         #is this path valid? (vertex between both points)
            if self.graph[path[pos - 1]][v] == 0:
                return False

            if v in path:                               #already visited (breaks rules of hamiltonian circuit)
                return False

            return True

        V = len(self.graph)          #vertices
        path = [-1] * V         #init
        path[0] = 0

        if not hamiltonian_util(path, 1):       #check path from 1
            return False

        print("hamiltonian circuit found: ", end="") #print circuit if exists
        for vertex in path:
            print(vertex, end=", ")
        print(path[0]) 
        return True
    def chromatic(self):
        colors = [-1] * len(self.graph)
        used_colors = set()

        for vertex in range(len(self.graph)):
            available_colors = set(range(len(self.graph)))       #by using sets, avoid repitition
            for neighbor in self.graph[vertex]:
                if colors[neighbor] != -1:
                    available_colors.discard(colors[neighbor])      #eliminate not-available possibilities

            if available_colors:
                color = min(available_colors)           #find the smallest one you can use (greedy)
            else:
                color = max(used_colors) + 1

            colors[vertex] = color
            used_colors.add(color) 

        chromatic_number = len(used_colors)
        return chromatic_number
                

# TESTING

#import file
FILENAME = 'test_graph.txt'
file = open(FILENAME)
file.seek(0)
g = Graph(int(file.readline())) #create blank graph

#add edges
l = file.readlines()
for line in l:
    g.add_edge(int(line.split()[0]) - 1, int(line.split()[1]) - 1)

euler = g.is_eulerian_circuit()
hamiltonian = g.is_hamiltonian()
chromatic = g.chromatic()


