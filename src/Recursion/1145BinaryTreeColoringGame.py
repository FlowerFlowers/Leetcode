'''
leetcode编号：1145
有一颗二叉树，A,B依次选择一个节点染色，A染红色，B染蓝色，然后再依次染色，
后一次染色的节点只能是之前节点的儿子或者父母，直到没有节点满足要求就换一个节点的儿子或者父亲继续
（依旧是A红色，B蓝色），直到没得选就结束了
问在A先手的情况选择了的下，B能不能稳赢
二叉树一共n（奇数）个节点，每个节点的值是1-n中的一个，x是a染色的第一个节点
思路：
A染色后，B选择A的儿子或者父母的一个点染色，然后这颗子树就都是B的了，其他是A的
只需要比较三颗子树的节点数量最大值能不能达到n+1/2
可以递归的访问节点，返回值是该节点为根的子树包含的节点个数，如果node.val=x , 那么这时候它的左右子树的返回值就是左右子树的大小

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        #flag 记录是不是已经找到了x
        c =[0,0]
        def count(node):
            #递归的底层，不包括节点
            if not node:
                return 0
            count_l, count_r = count(node.left), count(node.right)
            #发现了x节点
            if node.val ==x:
                c[0] = count_l
                c[1] = count_r
            #每个节点为根的子树，包括的节点数是left+right+1
            return count_r+count_l+1
        count(root)
        max_len = max(c[0], c[1], n-c[0]-c[1]-1)
        return max_len > n/2




