'''
leetcode编号232
使用两个栈构造一个队列
思路：
一个instack负责插入元素，一个outstack负责输出元素
需要弹出元素的时候：
1.如果outstack有元素，就弹出最上面的元素
2.如果outstack为空，就把instack的元素逐一插入outstack，这样子本来后入栈的元素就跑到了outstack的底部，先入栈的跑到了顶部，
那么outstack顶部的就应该是应该满足先进先出的元素


'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.outStack.pop(-1)


    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.inStack) and (not self.outStack)

    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop(-1))

que = MyQueue()
que.push(1)
que.push(2)
que.peek()
que.pop()
print(que.empty())
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()