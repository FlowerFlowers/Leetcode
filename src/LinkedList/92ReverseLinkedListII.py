'''
leetcode编号：92
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #如果只有一个节点
        if not head or not head.next or m == n:
            return head
        #设置一个哑节点的目的是保证就算m=1，也能正确的找到开始reverse的位置
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node
        for i in range(m-1):
            pre = pre.next
        cur = pre.next
        #break_node记录断开前的位置
        break_node = pre
        start_node = cur
        break_node.next = None
        #pre设置none很关键，初始化要反转的部分，和之前没联系
        pre = None
        for j in range(n-m+1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        break_node.next = pre
        start_node.next = cur
        #返回的一定是dummy_node.next，而不是head，因为head可能也参与了反转
        return dummy_node.next

