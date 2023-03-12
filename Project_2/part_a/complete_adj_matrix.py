class adj_matrix:
    def __init__(self, num_nodes):
        self.numNodes = num_nodes
        self.nodes = range(num_nodes)
        self.adj_mat = []

        for i in range(self.numNodes):
            self.adj_mat.append([1] * num_nodes)
            self.adj_mat[i][i] = 0

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
    graph.print_graph()
