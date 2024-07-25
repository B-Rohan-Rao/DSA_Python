class Graph:
    def __init__(self):
        """This method is just going to create an empty graph.
        It can be shown as{}.
        Further we are going to add vertex in this which can be visualized as this
         {
         'A' : []
         }                   """
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        """
        The concept here is that when a vertex is passed as a parameter,
        the first loop iterates through the list associated with that vertex and stores the value in 'other_vertex':
        {
            'A': ['B', 'D'],
            'B': ['A', 'C', 'D'],
            'C': ['B', 'D'],
        ->  'D': ['A', 'B', 'C']
        }
        The value stored in 'other_vertex' is then searched among the keys of the dictionary, and the connections
        are broken accordingly.
        :param vertex:
        :return:
        """
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])


my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 1)

my_graph.print_graph()

my_graph.remove_edge(1, 3)
my_graph.remove_edge(1, 4)
my_graph.remove_vertex(4)
my_graph.print_graph()
