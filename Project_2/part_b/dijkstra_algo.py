import adjacency_list
import heapq
import random
import time
import json

def randomGraphGenerator(size):
    graph= adjacency_list.LinkedList(size)
    for node in range(size):
        for adjacentNode in range(size):
            if adjacentNode==node:
                continue
            if random.randint(1,10)>5:
                weight= random.randint(0,100)
                graph.add_edge(node,adjacentNode,weight)
    return graph

def printHeap(heap,size):
    print(heapq.nsmallest(size,heap))

def printOrder(order):
    print()
    print('START ', end ="")
    for node in order:
        print('->',node, end ="")

def DijkstraAlgo(graph, startNode):
    distanceToNode={}
    preceedingNode={}
    solutionSet={}
    priorityQueue=[]
    orderNode=[]
    orderWeight=[]
    for node in graph.get_nodes():
        distanceToNode[node]=float('inf')
        preceedingNode[node]=None
        solutionSet[node]=0
    distanceToNode[startNode]=0
    for node in distanceToNode:
        nodeTup= (distanceToNode[node],node) #heapq elements: (weight, node) 
        heapq.heappush(priorityQueue,nodeTup)
    #printHeap(priorityQueue,graph.get_size())
    while (priorityQueue):
        cheapestNode= heapq.heappop(priorityQueue)
        solutionSet[cheapestNode[1]]=1
        orderNode.append(cheapestNode[1])
        orderWeight.append(cheapestNode[0])
        for adjacentNode in graph.adjacent_nodes(cheapestNode[1]): #adjacentNode:(node,weight) 
            if (solutionSet[adjacentNode[0]]==0 and distanceToNode[adjacentNode[0]]>distanceToNode[cheapestNode[1]]+ adjacentNode[1]):
                targetTup=(distanceToNode[adjacentNode[0]],adjacentNode[0])
                priorityQueue.remove(targetTup) #remove element from heapq
                #update both heapq and distance of shorter path
                distanceToNode[adjacentNode[0]]=distanceToNode[cheapestNode[1]]+ adjacentNode[1]
                nodeTup= (distanceToNode[adjacentNode[0]],adjacentNode[0]) 
                heapq.heappush(priorityQueue,nodeTup)
    #printOrder(orderNode)
    #printOrder(orderWeight)


result={}
print("Start")
for item in range(100,10000,100):
    print('at',item)
    graph= randomGraphGenerator(item)
    #graph.print_graph()
    start=time.time()
    DijkstraAlgo(graph,0)
    end=time.time()
    elapsed=end-start
    result[item]=elapsed
with open('data.json', 'w') as f:
    json.dump(result, f)
print("Completed")