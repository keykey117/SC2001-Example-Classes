import heapq
import random
import time
import json
import networkx as nx

def randomGraphGenerator(size, seed):
    g = nx.erdos_renyi_graph(size, 0.5, seed=seed, directed=False)
    for (u, v, w) in g.edges(data=True):
        w['weight'] = random.randint(1, 100)
    graph= nx.to_dict_of_dicts(g)
    return graph
def randomWorstGraphGenerator(size):
    g = nx.complete_graph(size)
    for (u, v, w) in g.edges(data=True):
        w['weight'] = random.randint(1, 100)
    graph= nx.to_dict_of_dicts(g)
    return graph
def randomSparseGraphGenerator(size):
    g = nx.path_graph(size)
    for (u, v, w) in g.edges(data=True):
        w['weight'] = random.randint(1, 100)
    graph= nx.to_dict_of_dicts(g)
    return graph
  
def printHeap(heap,size):
    print(heapq.nsmallest(size,heap))

def printOrder(order):
    print()
    print('START ', end ="")
    for node in order:
        print('->',node, end ="")

def DijkstraAlgo(graph, startNode, numNodes):
    distanceToNode={}
    preceedingNode={}
    solutionSet={}
    priorityQueue=[]
    orderNode=[] 
    orderWeight=[]
    for node in range(numNodes):
        distanceToNode[node]=float('inf')
        preceedingNode[node]=None
        solutionSet[node]=0
    distanceToNode[startNode]=0
    for node in distanceToNode:
        nodeTup= (distanceToNode[node],node)
        heapq.heappush(priorityQueue,nodeTup)
    while (priorityQueue):
        cheapestNode= heapq.heappop(priorityQueue)
        if (solutionSet[cheapestNode[1]]==1):
            continue
        solutionSet[cheapestNode[1]]=1
        orderNode.append(cheapestNode[1])
        orderWeight.append(cheapestNode[0])
        for adjacentNode in graph[cheapestNode[1]]:
            if (distanceToNode[adjacentNode]> distanceToNode[cheapestNode[1]]+ graph[cheapestNode[1]][adjacentNode]['weight']):
                distanceToNode[adjacentNode]=distanceToNode[cheapestNode[1]]+ graph[cheapestNode[1]][adjacentNode]["weight"]
                nodeTup= (distanceToNode[adjacentNode],adjacentNode) 
                heapq.heappush(priorityQueue,nodeTup)





# result={}
# print("Start")
# for item in range(100,6000,200):
#     print('at',item)
#     #first round
#     graph1= randomGraphGenerator(item, 50)
#     #graph1= randomWorstGraphGenerator(item)
#     start1=time.time()
#     DijkstraAlgo(graph1,0,item)
#     end1=time.time()
#     elapsed1=end1-start1
#     #second round
#     graph2= randomGraphGenerator(item, 100)
#     #graph2= randomWorstGraphGenerator(item)
#     start2=time.time()
#     DijkstraAlgo(graph2,0,item)
#     end2=time.time()
#     elapsed2=end2-start2

#     graph3= randomGraphGenerator(item, 150)
#     #graph3= randomWorstGraphGenerator(item)
#     start3=time.time()
#     DijkstraAlgo(graph3,0,item)
#     end3=time.time()
#     elapsed3=end3-start3
#     result[item]=(elapsed1 + elapsed2 + elapsed3)/3
# with open('dataNew6k.json', 'w') as f:
#     json.dump(result, f)
# print("Completed")

size=10000
#graph1= randomGraphGenerator(size, 50)
graph1= randomWorstGraphGenerator(size)
#graph1= randomSparseGraphGenerator(size)
start1=time.time()
DijkstraAlgo(graph1,0,size)
end1=time.time()
elapsed1=end1-start1
#second round
#graph2= randomGraphGenerator(size, 100)
graph2= randomWorstGraphGenerator(size)
#graph2= randomSparseGraphGenerator(size)
start2=time.time()
DijkstraAlgo(graph2,0,size)
end2=time.time()
elapsed2=end2-start2
#graph3= randomGraphGenerator(size, 150)
graph3= randomWorstGraphGenerator(size)
#graph3= randomSparseGraphGenerator(size)
start3=time.time()
DijkstraAlgo(graph3,0,size)
end3=time.time()
elapsed3=end3-start3
print('Time taken for Dijkstra Algorithm with Adjacency List and Minimizing Heap on a complete graph of size 10k')
print('Round 1: %.3f s' %elapsed1)
print('Round 2: %.3f s' %elapsed2)
print('Round 3: %.3f s' %elapsed3)
avg= (elapsed1+elapsed2+elapsed3)/3
print('Avg Time Taken: %.3f s'%avg)