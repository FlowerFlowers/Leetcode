'''
leetcode题号：142
给一个单链表，如果无环返回none 如果有环返回环开始的节点
思路：
类似141 ，先让walker和runner相遇
然后wakler1从head开始走，wakler2从相遇点开始走
两个指针相遇的地方就是环开始的节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        walker = head
        runner = head
        meet = None
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                meet = runner
                break
        if meet is None:
            return None
        else:
            pos = 0
            walker1 = meet
            walker2 = head
            while walker1 != walker2:
                walker1 = walker1.next
                walker2 = walker2.next
            return walker2

