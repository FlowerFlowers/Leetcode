'''
leetcode 206
反转链表
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

思路1.直接把路径上遇到的节点都用stack存储起来，然后到底了反着来一遍

思路2：访问一个就改造一个

思路3：递归到最后然后改
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#思路1：
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         node = head
#         StackAndQueue = []
#         if node is None:
#             return None
#         while node.next:
#             StackAndQueue.append(node)
#             node = node.next
#         revers_head = node
#         while StackAndQueue:
#             temp_node = StackAndQueue.pop(-1)
#             node.next = temp_node
#             temp_node.next = None
#             node = temp_node
#         return revers_head

#思路2：
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         #特殊情况
#         if head is None:
#             return None
#         if head.next is None:
#             return head
#         cur = head.next
#         pre = head
#         pre.next = None
#         while cur:
#             temp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = temp
#         return cur


#思路3：
class Solution:
    #递归的过程中函数的返回值一直都是最后一个node，只不过递归的过程中顺便改变指针，反转
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        next_node = head.next
        next_node.next = head
        head.next = None
        return new_head
