'''
leetcode题号：707
设计链表
思路：
创建node类，有val 和next两个属性，作为链表的基本单元
创建LinkedList类，有head和size属性记录列表开始的位置和大小
备注：leetcode有一个测试用例有问题
["MyLinkedList","addAtIndex","get","deleteAtIndex"]
[[],[-1,0],[0],[-1]]
[null,null,0,null]应该是[null,null,-1,null]

'''
#创建一个node类
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self,):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        #如果索引越界，返回-1
        if index < 0 or index >= self.size:
            return -1
        #从头开始取到第index个node
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val





    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        #在头部插入一个节点，只需要新建一个node，然后让链表第头之乡这就行了
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size +=1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        cur = self.head
        #如果链表为空，那么node作为第一个节点
        if cur == None:
            self.head = node
        #如果非空，node插入最后
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next=node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index-1):
                cur=cur.next
            node = Node(val)
            node.next = cur.next
            cur.next = node
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        bef = self.head
        if index == 0:
            self.head = bef.next
        else:
            for i in range(index-1):
                bef = bef.next
            bef.next = bef.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()
linkedList.addAtIndex(-1, 0)  # linked list becomes 1->2->3
linkedList.get(0)
linkedList.addAtIndex(0, 2)
cur = linkedList.head
for i in range(linkedList.size):
    print(cur.val,"->",end='')
    cur = cur.next
# linkedList.get(1)            # returns linkedList.addAtIndex(1, 10)2
# linkedList.get(2) # now the linked list is 1->3
# linkedList.get(2)# returns 3

