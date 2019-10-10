'''
leetcode题号 101
判断一颗树是不是对称的
eg:
    1
   / \
  2   2
 / \ / \
3  4 4  3
对称

    1
   / \
  2   2
   \   \
   3    3
不对称

思路1：BFS一层一层遍历，每一层的节点存在一个queue里,然后差看是否对称，直到遍历完（queue=[]）如果都是对称的那么就是对称的

思路2：
eg:
           1
       /       \
     2         2
   /    \     /  \
  3    4     4   3
 / \ / \   / \ /  \
5  6 7  8 8  7 6   5
分析：两个3的node应该是对称的，两个2的node应该是对称的，所以我们只需要一个stack存储node的对进行比较即可
比如我从stack中拿出[node3-1,node3-2]  只需要node3-1.left = node3-2.right  node3-1.right = node3-2.left即可
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# #思路1
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         #如果没有根
#         if not root:
#             return True
#         else:
#             if root.left == None and root.right ==None:
#                 return True
#             if root.left == None or root.right ==None:
#                 return False
#             que = [root.left, root.right]
#             while que:
#                 val_list = []
#                 for node in que:
#                     if node == None:
#                         val_list.append(None)
#                     else:
#                         val_list.append(node.val)
#                 for i in range(int(len(val_list) / 2)):
#                     if val_list[i] != val_list[len(val_list) - 1 - i]:
#                         return False
#                 temp_list = []
#                 for j in que:
#                     if j is not None:
#                         temp_list.append(j.left)
#                         temp_list.append(j.right)
#                 que = temp_list
#             return True

#思路2
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            #这个地方易错，如果都是none也只说明来这一对的问题，不能直接返回true，stack里还有其他
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(-1,[left.left,right.right])
                stack.insert(-1,[left.right,right.left])
            else:
                return False
        return True






