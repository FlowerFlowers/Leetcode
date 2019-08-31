'''
leetcode编号：160
eg：
Input: listA = [0,9,1,2,4], listB = [3,2,4]
Output: 值为2的node

Input: listA = [2,6,4], listB = [1,5]
Output: null
思路：关键是发现如果两个链表可以重合，重合后一摸一样，那么长的链表多出去那部分肯定没用
'''

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #先看那个链表更长，因为两个链表后来会合并，意味着合并后的部分一摸一样
        cur_a,cur_b = headA, headB
        len_a, len_b = 0, 0
        while cur_a is not None:
            cur_a = cur_a.next
            len_a +=1
        while cur_b is not None:
            cur_b = cur_b.next
            len_b += 1
        #更长的链表多出去多部分先走完
        cur_a = headA
        cur_b = headB
        if len_a > len_b:
            for i in range (len_a-len_b):
                cur_a = cur_a.next
        else:
            for i in range (len_b-len_a):
                cur_b = cur_b.next
        #如果两个节点不重合就往下走
        while cur_a != cur_b:
            cur_a = cur_a.next
            cur_b = cur_b.next
        return  cur_a