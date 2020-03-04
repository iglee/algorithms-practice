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
        if self.head != None:
            try:
                x = self.queue.pop(0)
		if self.queue[0] != None:
                    self.head = self.queue[0]
                else:
                    self.head = None
                return x
	    except:
                print("there's nothing left in the queue!")
                return None
