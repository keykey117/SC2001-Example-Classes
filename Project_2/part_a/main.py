import random
import time
import json
import adj_matrix
import priority_queue
import complete_adj_matrix
import networkx as nx


def randomSparseGraphGenerator(size):
    g = nx.path_graph(size)
    adj_mat = []
    for i in range(size):
        adj_mat.append([0]*size)
    for (u, v, w) in g.edges(data=True):
        adj_mat[u][v] = random.randint(1, 100)

    graph = adj_matrix.sparse_adj_matrix(size, adj_mat)

    return graph


def randomGraphGenerator(size):
    graph = adj_matrix.adj_matrix(size)
    for node in range(size):
        for adjacentNode in range(size):
            if adjacentNode == node:
                continue
            if random.randint(1, 10) > 5:
                weight = random.randint(0, 100)
                graph.add_edge(node, adjacentNode, weight)
    return graph


def printOrder(order):
    print()
    print('START ', end="")
    for node in order:
        print('->', node, end="")


def DijkstraAlgo(graph, startNode):
    distanceToNode = {}
    preceedingNode = {}
    solutionSet = {}
    pq = priority_queue.PriorityQueue()
    orderNode = []
    orderWeight = []
    for node in graph.get_nodes():
        distanceToNode[node] = float('inf')
        preceedingNode[node] = None
        solutionSet[node] = 0
    distanceToNode[startNode] = 0
    for node in distanceToNode:
        # queue elements: (weight, node)
        nodeTup = (distanceToNode[node], node)
        pq.insert(nodeTup)
    while (not pq.isEmpty()):
        cheapestNode = pq.delete()
        solutionSet[cheapestNode[1]] = 1
        orderNode.append(cheapestNode[1])
        orderWeight.append(cheapestNode[0])
        # adjacentNode:list of weights
        for adjacentNode, weight in enumerate(graph.adjacent_nodes(cheapestNode[1])):
            if weight == 0:
                continue
            if (solutionSet[adjacentNode] == 0 and
                    distanceToNode[adjacentNode] > distanceToNode[cheapestNode[1]] + weight):
                targetTup = (distanceToNode[adjacentNode], adjacentNode)
                pq.remove(targetTup)  # remove element from priority q
                # update both priority q and distance of shorter path
                distanceToNode[adjacentNode] = distanceToNode[cheapestNode[1]] + weight
                nodeTup = (distanceToNode[adjacentNode], adjacentNode)
                pq.insert(nodeTup)


# result = {}
# print("Start")
# # for item in range(100, 10000, 100):
# #     print('at', item)
# #     graph = randomGraphGenerator(item)
# #     # graph.print_graph()
# #     start = time.time()
# #     DijkstraAlgo(graph, 0)
# #     end = time.time()
# #     elapsed = end-start
# #     result[item] = elapsed
# # with open('data.json', 'w') as f:
# #     json.dump(result, f)
# print("Completed")

size = 5000
#graph1= randomGraphGenerator(size, 50)
#graph1 = complete_adj_matrix.complete_adj_matrix(size)
graph1 = randomSparseGraphGenerator(size)
start1 = time.time()
DijkstraAlgo(graph1, 0)
end1 = time.time()
elapsed1 = end1-start1
print('Round 1: %.3f s' % elapsed1)
# second round
#graph2= randomGraphGenerator(size, 100)
#graph2 = complete_adj_matrix.complete_adj_matrix(size)
graph2 = randomSparseGraphGenerator(size)
start2 = time.time()
DijkstraAlgo(graph2, 0)
end2 = time.time()
elapsed2 = end2-start2
print('Round 2: %.3f s' % elapsed2)
#graph3= randomGraphGenerator(size, 150)
#graph3 = complete_adj_matrix(size)
graph3 = randomSparseGraphGenerator(size)
start3 = time.time()
DijkstraAlgo(graph3, 0)
end3 = time.time()
elapsed3 = end3-start3
print('Round 3: %.3f s' % elapsed3)
print('Time taken for Dijkstra Algorithm with Adjacency matrix and array on a sparse graph of size '+str(size))
print('Round 1: %.3f s' % elapsed1)
print('Round 2: %.3f s' % elapsed2)
print('Round 3: %.3f s' % elapsed3)
avg = (elapsed1+elapsed2+elapsed3)/3
print('Avg Time Taken: %.3f s' % avg)
