# domain (u,v,e)
def from_edges(edges):
    graph = {}
    for u, v, *w in edges:
        w = w[0] if w else None

        if(v and v not in graph):
            graph[v] = []

        children = []
        if(u in graph):
            children = graph[u]
        else:
            graph[u] = children
        children.append(v)

    return graph


def mark_all_unvisited(graph):
    for visited, _ in graph.values():
        visited[0] = False


counter = 1


def dfs(graph, v):
    visited, children = graph[v]
    if(not visited[0]):
        visited[0] = True
        print(v)

        for child, _ in children:
            dfs(graph, child)


def dfs_all(graph):
    print(graph)
    for vertex, (visited, _) in graph.items():
        if(not visited[0]):
            dfs(graph, vertex)
        mark_all_unvisited(graph)
        global counter
        counter = 1
        print("-------")


print(dfs_all(from_edges([
    ('A', 'B'), ('A', 'E'), ('E', 'I'), ('I', 'J'), ('J', 'E')
])))
