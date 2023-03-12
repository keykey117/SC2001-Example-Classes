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
    orderNode=[] #for tracking
    orderWeight=[] #for tracking
    for node in range(numNodes):
        distanceToNode[node]=float('inf')
        preceedingNode[node]=None
        solutionSet[node]=0
    distanceToNode[startNode]=0
    for node in distanceToNode:
        nodeTup= (distanceToNode[node],node) #heapq elements: (weight, node) 
        heapq.heappush(priorityQueue,nodeTup)
    #printHeap(priorityQueue,graph.get_size())
    while (priorityQueue):
        cheapestNode= heapq.heappop(priorityQueue)#(weight, node) 
        solutionSet[cheapestNode[1]]=1
        orderNode.append(cheapestNode[1])
        orderWeight.append(cheapestNode[0])
        for adjacentNode in graph[cheapestNode[1]]:
            if (solutionSet[adjacentNode]==0 and distanceToNode[adjacentNode]> distanceToNode[cheapestNode[1]]+ graph[cheapestNode[1]][adjacentNode]['weight']):
                targetTup=(distanceToNode[adjacentNode],adjacentNode)
                priorityQueue.remove(targetTup) #remove element from heapq
                #update both heapq and distance of shorter path
                distanceToNode[adjacentNode]=distanceToNode[cheapestNode[1]]+ graph[cheapestNode[1]][adjacentNode]["weight"]
                nodeTup= (distanceToNode[adjacentNode],adjacentNode) 
                heapq.heappush(priorityQueue,nodeTup)
    # printOrder(orderNode)
    # printOrder(orderWeight)




result={}
print("Start")
for item in range(100,2000,50):
    print('at',item)
    #first round
    graph1= randomGraphGenerator(item, 50)
    start1=time.time()
    DijkstraAlgo(graph1,0,item)
    end1=time.time()
    elapsed1=end1-start1
    #second round
    graph2= randomGraphGenerator(item, 100)
    start2=time.time()
    DijkstraAlgo(graph2,0,item)
    end2=time.time()
    elapsed2=end2-start2

    graph3= randomGraphGenerator(item, 150)
    start3=time.time()
    DijkstraAlgo(graph3,0,item)
    end3=time.time()
    elapsed3=end3-start3

    result[item]=(elapsed1 + elapsed2 + elapsed3)/3
with open('data.json', 'w') as f:
    json.dump(result, f)
print("Completed")