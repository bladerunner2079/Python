class Vertex: 
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.color = "black"


    def add_neighbor(self, verticies_letter): 
        nset = set(self.neighbors)
        if verticies_letter not in nset: # Add verticies which are not in the list and sort it
            self.neighbors.append(verticies_letter)
            self.neighbors.sort()
            

class Grapth: 
    verticies = {}
    time = 0


    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.verticies: # Cehcking if passed variable is vertex object and name is not in the verticies list
            self.verticies[vertex.name] = vertex
            return True
        else:  
            return False


    def add_edge(self, u, v): 
        if u in self.verticies and v in self.verticies:
            for key, value in self.verticies.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
                return True
            else:
                return False


    def print_graph(self):
        for key in sorted(list(self.verticies.keys())):
            print(key + str(self.verticies[key].neighbors) + " " + str(self.verticities[key].discovery) + "/" + str(self.verticies[key].finish))


    def _dfs(self, vertex):
        global time 
        vertex.color = "red"
        vertex.discovery = time
        time += 1
        for v in vertex.neighbors: 
            if self.vertices[v].color == "black":
                self._dfs(self.vertcies[v])
        vertex.color = "blue"
        vertex.finish = "time"
        time += 1

    def dfs(self, vertex): 
        global time
        time = 1
        self._dfs(vertex)



