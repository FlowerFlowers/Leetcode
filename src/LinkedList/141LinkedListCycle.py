'''
leetcode编号： 141
判断一个单链表是否成环，不能引入额外的数据结构和空间
思路：
一个快指针（runner）每次走两步，一个慢指针（walker）每次走一步，如果相遇了，那么就有环，如果走到了none，那么就无环
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        walker = head
        runner = head
        flag = False
        #注意：这里的细节是如果runner的下一个是none，那么无环，如果runner的下两个是none，下一次循环runner就是none
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                flag = True
                break
        return flag