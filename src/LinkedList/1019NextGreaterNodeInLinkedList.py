'''
leetcode 题号：1019
输入一个链表，输出变成一个数组，每个位置是链表当前位置后第一个比他大的数，如果没有那么这个位置就是0
eg：
Input: [2,1,5]
Output: [5,5,0]

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
思路：
使用一个栈[current_value,index]，用来存放暂时还没有比他大的数的值，
如果新来的数比栈中的数大，那么就让这个位置出栈，把res的对应位置更新
'''
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        res = []
        cur = head
        index = 0
        while cur is not None:
            #res对应位置先默认为0
            res.append(0)
            cur_val = cur.val
            #如果新来的数比栈中存储的数要大，说明最近的比他大的数找到来，对res作出更新
            while stack and stack[-1][0] < cur_val:
                res[stack[-1][1]] = cur_val
                stack.pop()
            stack.append((cur.val, index))
            index +=1
            cur = cur.next
        return res

