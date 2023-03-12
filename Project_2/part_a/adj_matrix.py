class sparse_adj_matrix:
    def __init__(self, num_nodes, graph):
        self.numNodes = num_nodes
        self.nodes = range(num_nodes)
        self.adj_mat = graph

        # for i in range(self.numNodes):
        #     self.adj_mat.append([0] * num_nodes)

    def get_size(self):
        return self.numNodes

    def get_nodes(self):
        return self.nodes

    def get_size(self):
        return self.numNodes

    def add_edge(self, start, end, weight):
        self.adj_mat[start][end] = weight

    def adjacent_nodes(self, node):
        return self.adj_mat[node]

    def print_graph(self):
        for node in range(len(self.adj_mat)):
            print("node", node, "- ", self.adj_mat[node])


class adj_matrix:
    def __init__(self, num_nodes, graph):
        self.numNodes = num_nodes
        self.nodes = range(num_nodes)
        self.adj_mat = []

        for i in range(self.numNodes):
            self.adj_mat.append([0] * num_nodes)

    def get_size(self):
        return self.numNodes

    def get_nodes(self):
        return self.nodes

    def get_size(self):
        return self.numNodes

    def add_edge(self, start, end, weight):
        self.adj_mat[start][end] = weight

    def adjacent_nodes(self, node):
        return self.adj_mat[node]

    def print_graph(self):
        for node in range(len(self.adj_mat)):
            print("node", node, "- ", self.adj_mat[node])


if __name__ == "__main__":
    graph = adj_matrix(5)  # follows Lect 6 Slide 11
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 4, 5)
    graph.add_edge(1, 4, 2)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 4)
    graph.add_edge(3, 2, 6)
    graph.add_edge(3, 0, 7)
    graph.add_edge(4, 3, 2)
    graph.add_edge(4, 1, 3)
    graph.add_edge(4, 2, 9)
    graph.print_graph()
