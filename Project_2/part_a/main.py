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
            if (solutionSet[adjacentNode] == 0 and distanceToNode[adjacentNode] > distanceToNode[cheapestNode[1]] + weight):
                targetTup = (distanceToNode[adjacentNode], adjacentNode)
                pq.remove(targetTup)  # remove element from priority q
                # update both priority q and distance of shorter path
                distanceToNode[adjacentNode] = distanceToNode[cheapestNode[1]] + weight
                nodeTup = (distanceToNode[adjacentNode], adjacentNode)
                pq.insert(nodeTup)
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
