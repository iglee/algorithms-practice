class Q:
    # queue = FIFO (first in first out)
    def __init__(self):
        self.queue = []
        self.head = None
        self.rear = None        
    def enqueue(self, x):
        self.queue.append(x)
        if self.head == None:
            self.head = x
        self.rear = x

    def dequeue(self):
        if self.queue:
            if len(self.queue)>1:
	    	self.head = self.queue[1]
            else:
                self.head = None
		self.rear = None
            return self.queue.pop(0)

if __name__ == "__main__":

    q = Q()
    print("add element ", 1)
    q.enqueue(1)
    print("add element ", 2)
    q.enqueue(2)
    print("add element ", 13)
    q.enqueue(13)
    print("add element ", 4)
    q.enqueue(4)
    print("add element ", 9)
    q.enqueue(9)
    print("add element ", 0)
    q.enqueue(0)
    print("current queue : ",q.queue)
    for x in range(6):
        print(q.dequeue())
        print("current head : ", q.head)
        print("current rear : ", q.rear)
