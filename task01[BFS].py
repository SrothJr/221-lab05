from collections import deque
# Kahn's algorithm for topological sorting: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

def topsort_bfs(adj, v):
    indeg = [0] * len(adj)        #.....For storing indegree values, only values with 0 indegrees can be enqued first. 
    for i in adj:           
        for j in i:
            indeg[j] += 1

    q = deque()             #.....Creating a queue, queue works as backbone of BFS, (Because "First In First Out")
    for i in range(v):
        if indeg[i] == 0:   #.....Only enqueing values with 0 indegree first (Zero Indegree = No requirments)
            q.append(i)

    order = []      #.....To store the resulting list
    while q:
        node = q.popleft()      #.....Dequeing the first value of the queue
        order.append(node)      #.....Adding values with ZERO Indegree to resulting list, Zero indegree = Can be done now!

        for a in adj[node]:
            indeg[a] -= 1         #.....Everytime we find a value, we reduce its indegree as one of the requirments were met
            if indeg[a] == 0:     #.....No indegree means, All requirments met
                q.append(a)

    return order

input_file = open("input01[2].txt", "r")
output_file = open("output01[2].txt", "w")

n, m = [int(i) for i in input_file.readline().strip().split(" ")]

# print(n, m) [For debugging]
edges = []

#.....Storing the edges in a multi-dimention list
for i in range(m):
    edges.append([int(i) for i in input_file.readline().strip().split(" ")]) 

adj = [[] for _ in range(n+1)]

for i in edges:
    adj[i[0]].append(i[1])

#print(adj) [for debugging]

order = topsort_bfs(adj, n+1)

if len(order) != n+1:
    print("IMPOSSIBLE", file=output_file)
else:
    for i in order:
        print(i, end=" ", file=output_file)