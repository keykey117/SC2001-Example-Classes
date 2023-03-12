import networkx as nx
import random
#G = nx.erdos_renyi_graph(10, 0.5, seed=123, directed=False) #nodes, probability
G = nx.complete_graph(5)
for (u, v, w) in G.edges(data=True):
    w['weight'] = random.randint(1, 100)
A = nx.adjacency_matrix(G).toarray()
D = nx.to_dict_of_dicts(G)
print(A)
print(D)
G = nx.path_graph(5)
A = nx.adjacency_matrix(G).toarray()
D = nx.to_dict_of_dicts(G)
print(A)
print(D)