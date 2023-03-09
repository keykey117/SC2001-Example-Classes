#Linked List Structure: dictionary where keys are node and values are a list of dictionaries where key is the connected/adjacent node and value is the edge's weight

class LinkedList:
    def __init__(self,num_nodes):
        self.numNodes=num_nodes
        self.nodes=range(num_nodes)
        self.adjc_list={}
        for node in self.nodes:
            self.adjc_list[node]=[]
    def get_nodes(self):
        return self.nodes
    def get_size(self):
        return self.numNodes
    def add_edge(self, start, end, weight):
        self.adjc_list[start].append((end,weight))
    def adjacent_nodes(self,node):
        return self.adjc_list[node]
    def print_graph(self):
        for node in self.adjc_list.keys():
            print("node",node,"- " ,self.adjc_list[node])

if __name__ == "__main__":
    graph = LinkedList(5) #follows Lect 6 Slide 11
    graph.add_edge(0,1,10)
    graph.add_edge(0,4,5)
    graph.add_edge(1,4,2)
    graph.add_edge(1,2,1)
    graph.add_edge(2,3,4)
    graph.add_edge(3,2,6)
    graph.add_edge(3,0,7)
    graph.add_edge(4,3,2)
    graph.add_edge(4,1,3)
    graph.add_edge(4,2,9)
    graph.print_graph()
