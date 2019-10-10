'''
leetcode题号：863
给定一个根节点和target的值，找到距离这个target为k的节点的值
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

思路：
遍历一遍树，创建一个dict，负责记录每个节点的临近节点，然后由target发散寻找到距离为k的点
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        import collections
        conn = collections.defaultdict(list)
        #建立conn字典，记录每个节点邻近的节点
        def conncet(node):
            if node:
                if node.left:
                    conn[node.val].append(node.left.val)
                    conn[node.left.val].append(node.val)
                    conncet(node.left)
                if node.right:
                    conn[node.val].append(node.right.val)
                    conn[node.right.val].append(node.val)
                    conncet(node.right)
        conncet(root)
        #res记录最终的结果，seen记录已经见过的节点，因为看邻近节点的时候"回头路"不算
        res = [target.val]
        seen = set(res)
        while K > 0:
            temp = []
            for i in res:
                temp2 = [j for j in conn[i] if j not in seen]
                temp.extend(temp2)
            res = temp
            # | 对两个集合求并集
            seen = seen | set(res)
            K -= 1
        return res








