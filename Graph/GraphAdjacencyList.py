class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [None] * self.vertex

    def add_edge(self, a, b):
        node = AdjNode(b)
        node.next = self.graph[a]
        self.graph[a] = node


    def add_edges(self, src, dest):
        self.add_edge(src, dest)
        self.add_edge(dest, src)


    def print_graph(self):
        for i in range(self.vertex):
            print("Adjacency list of vertex ", str(i))
            string = str(i)
            itr = self.graph[i]
            while itr:
                string += " --> " + str(itr.data)
                itr = itr.next
            print(string)



if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edges(0, 1)
    graph.add_edges(0, 4)
    graph.add_edges(1, 2)
    graph.add_edges(1, 3)
    graph.add_edges(1, 4)
    graph.add_edges(2, 3)
    graph.add_edges(3, 4)

    graph.print_graph()

