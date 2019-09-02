'''
leetcode题号：725
把一个链表拆分成等长的几部分，如果不能整分，那么就前几个链表长1
eg：
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]

Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

思路：先获得链表的总长，然后确定各个子链表长度构造链表即可
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        len = 0
        cur = root
        #获得链表的长度
        while cur is not None:
            cur = cur.next
            len +=1

        #确定每个子链表的长度
        list_long,num = divmod(len,k)
        cur = root
        res = []

        #构造子链表
        while cur is not None:
            head = ListNode(cur.val)
            res.append(head)
            if num > 0:
                for i in range(list_long+1):
                    cur = cur.next
                    if i != list_long:
                        head.next = ListNode(cur.val)
                        head = head.next
            else:
                for i in range(list_long):
                    cur = cur.next
                    if i != list_long-1:
                        head.next = ListNode(cur.val)
                        head = head.next

            num -=1
        #特殊情况
        if k > len:
            for i in range(k-len):
                res.append(None)
        return res

