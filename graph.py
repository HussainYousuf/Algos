from collections import defaultdict


class Graph:

    def __init__(self) -> None:
        self.indegree = defaultdict(int)
        self.weight = defaultdict(dict)
        self.visited = defaultdict(bool)
        self.pre_num = defaultdict(int)
        self.post_num = defaultdict(int)
        self.counter = int()
        self.components = []

    def from_edges(self, edges):
        for u, v, *w in edges:
            if(u):
                self.indegree[u]
            if(v):
                self.weight[u][v] = w[0] if w else None
                self.indegree[v] += 1

    def get_counter(self):
        self.counter += 1
        return self.counter

    def dfs(self, u):
        weight = self.weight
        visited = self.visited
        pre_num = self.pre_num
        post_num = self.post_num

        visited[u] = True
        pre_num[u] = self.get_counter()
        for v in weight[u].keys():
            if(not visited[v]):
                self.dfs(v)
        post_num[u] = self.get_counter()

    def mark_all_unvisited(self):
        self.visited = defaultdict(bool)

    def reset_counter(self):
        self.counter = int()

    def dfs_all(self):
        visited = self.visited
        indegree = self.indegree
        for u in sorted(indegree, key=indegree.get):
            if(visited[u]):
                continue
            self.dfs(u)
            self.reset_counter()
            self.components.append(dict(self.pre_num))
            self.pre_num = defaultdict(int)
        self.mark_all_unvisited()

    def all_DAGs(self):
        weight = self.weight
        for component in self.components:
            for u, pre_num in component.items():
                cycle = False
                for v in weight[u].keys():
                    if(pre_num > component[v]):
                        cycle = True
                        print(f"break because of cycle from edge {u} to {v}")
                        break
                if(cycle):
                    break
                print(u)
            print("----------")


g = Graph()
g.from_edges([
    ('J', 'E'), ('A', 'E'), ('A', 'B'),
    ('E', 'I'), ('I', 'J'), ('F', None),
    ('C', 'D'),
])
g.dfs_all()
g.all_DAGs()
print(g.components)
