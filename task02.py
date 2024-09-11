import heapq as hq

def lex_topsort(adj):
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
        node = hq.heappop(o)
        top_ord.append(node)

        for i in adj[node]:
            indeg[i] -= 1

            if indeg[i] == 0:
                hq.heappush(o, i)

    if len(top_ord) != v:
        print("IMPOSSIBLE", file= output_file)
    else:
        for i in top_ord:
            print(i, end=" ", file= output_file)


input_file = open("input02.txt", "r")
output_file = open("output02.txt", "w")

n, m = [int(i) for i in input_file.readline().strip().split(" ")]

# print(n, m) [For debugging]
edges = []

#.....Storing the edges in a multi-dimention list
for i in range(m):
    edges.append([int(i) for i in input_file.readline().strip().split(" ")]) 

adj = [[] for _ in range(n)]

for i in edges:
    adj[i[0]].append(i[1])

lex_topsort(adj)
output_file.close()
