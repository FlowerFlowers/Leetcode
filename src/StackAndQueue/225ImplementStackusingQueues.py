'''
leetcode 题号 225
使用队列queques 构造 栈stack
'''
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto StackAndQueue.
        """
        if self.que1 != []:
            self.que1.append(x)
        else:
            self.que2.append(x)



    def pop(self) -> int:
        """
        Removes the element on top of the StackAndQueue and returns that element.
        """
        if self.que1 != []:
            while len(self.que1) > 1:
                self.que2.append(self.que1.pop(0))
            return self.que1.pop(0)
        else:
            while len(self.que2) > 1:
                self.que1.append(self.que2.pop(0))
            return self.que2.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.que1 != []:
            while len(self.que1) > 1:
                self.que2.append(self.que1.pop(0))
            res = self.que1.pop(0)
            self.que2.append(res)
            return res
        else:
            while len(self.que2) > 1:
                self.que1.append(self.que2.pop(0))
            res = self.que2.pop(0)
            self.que1.append(res)
            return res


    def empty(self) -> bool:
        """
        Returns whether the StackAndQueue is empty.
        """
        return (not self.que1) and (not self.que2)
