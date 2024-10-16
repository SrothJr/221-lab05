def cnvrt2graph(input_file): #.....COverting to a dictionary
    n, m = input_file.readline().strip().split(" ")

    graph = {} # creating the hosting graph
    for i in range(1, int(n)+1):
        graph[i] = []

    for i in range(int(m)):
        p, c = input_file.readline().strip().split(" ")
        graph[int(p)].append(int(c))

    return graph

def topsort(graph, ordering, visited):
    indeg = []
    for i in graph.values():
        for j in i:
            if j not in indeg:
                indeg.append(j)

    for i in graph.keys():
        if i not in indeg:
            dfs(graph, i, ordering, visited)
        

    for i in graph.keys():
        if i not in indeg:
            ordering.append(i)
            visited.append(i)
            


def dfs(graph, v, ordering, visited):
    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(graph, i, ordering, visited)
            ordering.append(i)

input_file = open("input/input01[DFS].txt", "r")
output_file = open("output/output01[DFS].txt", "w")
graph = cnvrt2graph(input_file)
ordering = []
visited = []
topsort(graph, ordering,visited)

if len(ordering) == len(graph):
    for i in range(len(ordering)-1, -1, -1):    #....Printing in reverse
        print(ordering[i], end=" ", file=output_file)
else:
    print("IMPOSSIBLE", end=" ", file=output_file)
