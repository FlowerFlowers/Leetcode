'''
leetcode：147
对链表进行插入排序
思路：
首先构造一个dummy_node用来作为链表的开始，dummy_node.next = head，因为之后的元素都可能改变，返回dummy_node.next作为链表的头是安全的
然后从第二个节点开始作为cur，之前的是pre，从dummy_node.next开始遍历，找到合适的插入位置，分为两种情况
1. 之前的节点值都小于cur.val，那么什么都不需要改变，cur后移一个，继续就行
2 . 需要cur插入中间，那么pre.next = cur.next 然后cur插入相应的位置即可
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        #0或1个元素不用排
        if not head or not head.next:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = head.next
        pre = head
        while cur:
            #temp_node 记录最后一个比cur小的node的位置
            temp_node = dummy_node
            while temp_node.next.val < cur.val and temp_node.next != cur:
                temp_node = temp_node.next
            #如果之前的数都比cur小，那么就什么也不用操作
            if temp_node.next == cur:
                pre = pre.next
                cur = cur.next
            #节点插入相应的位置
            else:
                pre.next = cur.next
                temp = temp_node.next
                temp_node.next = cur
                cur.next = temp
                cur = pre.next
        return dummy_node.next






