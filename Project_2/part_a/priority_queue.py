class PriorityQueue(object):
    def __init__(self, distanceToNode):
        self.queue = []
        self.distanceToNode = distanceToNode

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # remove specific element

    def remove(self, data):
        try:
            self.queue.remove(data)
        except:
            print()
            exit()

    # for popping an element based on Priority
    def pop(self):
        min_val = 0
        for i in range(len(self.queue)):
            if self.distanceToNode[self.queue[i]] < self.distanceToNode[self.queue[min_val]]:
                min_val = i
        item = self.queue[min_val]
        del self.queue[min_val]
        return item


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())
