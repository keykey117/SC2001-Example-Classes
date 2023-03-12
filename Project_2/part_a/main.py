import random
import time
import json
import adj_matrix
import priority_queue


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

    orderNode = []
    orderWeight = []
    for node in graph.get_nodes():
        distanceToNode[node] = float('inf')
        preceedingNode[node] = None
        solutionSet[node] = 0
    distanceToNode[startNode] = 0
    pq = priority_queue.PriorityQueue(distanceToNode)
    for node in distanceToNode:
        # queue elements: node
        pq.insert(node)

    while (not pq.isEmpty()):
        cheapestNode = pq.pop()
        solutionSet[cheapestNode] = 1
        orderNode.append(cheapestNode)
        orderWeight.append(distanceToNode[cheapestNode])
        # adjacentNode:list of weights
        for adjacentNode, weight in enumerate(graph.adjacent_nodes(cheapestNode)):
            if weight == 0:
                continue
            if (solutionSet[adjacentNode] == 0 and
                    pq.distanceToNode[adjacentNode] > pq.distanceToNode[cheapestNode] + weight):
                pq.distanceToNode[adjacentNode] = pq.distanceToNode[cheapestNode] + weight
                pq.insert(adjacentNode)
    # printOrder(orderNode)
    # printOrder(orderWeight)


result = {}
print("Start")
for item in range(100, 10000, 100):
    print('at', item)
    graph = randomGraphGenerator(item)
    # graph.print_graph()
    start = time.time()
    DijkstraAlgo(graph, 0)
    end = time.time()
    elapsed = end-start
    result[item] = elapsed
with open('data.json', 'w') as f:
    json.dump(result, f)
print("Completed")
