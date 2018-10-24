class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.color = "black"

    def add_neighbor(self, v):
        my_set = set(self.neighbors)
        if v not in my_set:
            self.neighbors.append(v)
            self.neighbors.sort()
        print(self.neighbors)

class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery)
                  + "  " + str(self.vertices[key].finish)
                  )

    def _dfs(self, vertex):
        global time
        print(time)
        vertex.color = "red"
        vertex.discovery = time
        time += 1

        for v in vertex.neighbors:
            if self.vertices[v].color == "black":
                self._dfs(self.vertices[v])
        vertex.color = "blue"
        vertex.finish = time
        time += 1

    def dfs(self, start_vertex):
        global time
        time = 1
        self ._dfs(start_vertex)


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.dfs(a)
g.print_graph()