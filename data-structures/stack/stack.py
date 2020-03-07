class S:
    def __init__(self):
        self.stack = []
        self.top = None

    def empty(self):
        if not self.stack:
            return True
        return False

    def push(self, x):
        self.stack.append(x)
        self.top = x

    def pop(self):
        if not self.empty():
	    if len(self.stack)>1:
		self.top = self.stack[-2]
	    else:
		self.top = None
            return self.stack.pop()
        return None
            

if __name__ == "__main__":
    s = S()
    print("add element : ", 1)
    s.push(1)
    print("add element : ", 13)
    s.push(13)
    print("add element : ", 4)
    s.push(4)
    print("add element : ", 9)
    s.push(9)
    print("add element : ", 7)
    s.push(7)

    for i in range(5):
        print("pop the latest element: ", s.pop())
        print("current top: ", s.top)

