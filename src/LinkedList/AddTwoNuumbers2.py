'''
leetcode编号：445
eg：
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
思路：先把链表里的数拿出来，然后代数运算出结果再放到链表里
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = 0
        sum2 = 0
        while l1 is not  None:
            sum1 = sum1*10+l1.val
            l1 = l1.next
        while l2 is not  None:
            sum2 = sum2*10+l2.val
            l2 = l2.next
        sum = str(sum1+sum2)
        head = ListNode(None)
        cur = head
        for i in range(len(sum)):
            cur.next = ListNode(int(sum[i]))
            cur = cur.next
        return head.next



