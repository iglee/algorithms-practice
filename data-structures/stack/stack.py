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
        if self.stack:
            if self.stack[-2]:
                self.top = self.stack[-2]
            else:
                self.top = None
            return  self.stack.pop()
            
        else:
            return None
