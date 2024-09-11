import heapq as hq #...Heap usages priority queue 

def lex_topsort(adj): #....From smallest to biggest value
    v = len(adj)
    indeg = [0] * v

    for i in range(v):
        for j in adj[i]:
            indeg[j] += 1

    o = []
    for i in range(v):
        if indeg[i] == 0:
            hq.heappush(o, i)

    top_ord = []

    while o:
        node = hq.heappop(o)        #.... Pops and returns the smallest value of the given list (o)
        top_ord.append(node)

        for i in adj[node]:
            indeg[i] -= 1

            if indeg[i] == 0:
                hq.heappush(o, i)

    if len(top_ord) != v:       #..... If the len of resulting list is not the same size as the total nodes, there's a cycle
        print("IMPOSSIBLE", file= output_file)
    else:
        for i in top_ord:
            print(i, end=" ", file= output_file)


input_file = open("input/input02.txt", "r")
output_file = open("output/output02.txt", "w")

n, m = [int(i) for i in input_file.readline().strip().split(" ")]

# print(n, m) [For debugging]
edges = []

#.....Storing the edges in a multi-dimention list
for i in range(m):
    edges.append([int(i) for i in input_file.readline().strip().split(" ")]) 

# Creating a adj-list which will store the destinations on the index same as the value of source
# Better works when values are from 0 - N and continuos 
adj = [[] for _ in range(n)]

for i in edges:
    adj[i[0]].append(i[1])

lex_topsort(adj)
output_file.close()
