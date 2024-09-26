class MyQueue:
   #TC:O(N) SC: O(N)
    def __init__(self):
        self.que = []
        self.que2 = []

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if not self.que2:
            while len(self.que) != 0:
                self.que2.append(self.que.pop())
        return self.que2.pop()

    def peek(self) -> int:
        if not self.que2:
            while len(self.que) != 0:
                self.que2.append(self.que.pop())
        return self.que2[-1]        

    def empty(self) -> bool:
        return not self.que and not self.que2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
