class Graph:

    def __init__(self):
        self.graph = {}
        self.size = 0

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set(())
            self.size += 1
        self.graph[u].add(v)

    def get_neighbors(self, node):
        return self.graph[node]
    
    def get_dist_two(self, node):
        neighbors = self.get_neighbors(node)
        dist_two = set(())
        for neighbor in neighbors:
            dist_two = dist_two.union(self.get_neighbors(neighbor))
        return dist_two
    
    def get_dist(self, v, u):
        dist = 0
        visited = set(())
        queue = [(v, 0)]
        while queue:
            node, d = queue.pop(0)
            if node == u:
                dist = d
                break
            visited.add(node)
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, d+1))
        return dist
    
    @staticmethod
    def make_from_file(filename):
        g = Graph()
        with open(filename, 'r') as f:
            for line in f:
                u, neighbors = line.split(':')
                for v in neighbors.strip().split(','):
                    g.add_edge(int(u), int(v))
                    g.add_edge(int(v), int(u))

        return g
    
    @staticmethod
    def make_from_adjacency_matrix(matrix):
        g = Graph()
        for u in range(len(matrix)):
            for v in range(len(matrix[u])):
                if int(matrix[u][v]) == 1:
                    g.add_edge(u, v)
        return g

    @staticmethod
    def calculate_diameter(g):
        diameter = 0
        for u in g.graph:
            for v in g.graph:
                if u != v:
                    dist = g.get_dist(u, v)
                    if dist > diameter:
                        diameter = dist
        return diameter