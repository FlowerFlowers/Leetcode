'''
leetcode编号：241
通过不同的结合方式，给出可能的结果
eg：
Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2


Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

思路：加括号确定运算顺序的本质其实就是哪个符号先用，哪个符号后用的问题
所以可以分而治之：
首先确定最后一个使用的符号，然后剩下两部分变成相同的问题，给出各自可能的结果，最后使用这个符号结合
递归到最底层，情况就是两部分变成单独的一个数，然后通过中间的符号运算即可

易错：递归到底层return[input] 返回的是list
'''
from typing import  List
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        #递归到底层，就是直接返回相应的数字
        if input.isdigit():
            return [(int(input))]
        res=[]
        #选择用那个符号分成两部分
        for i in range(len(input)):
            if input[i] in '+-*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                #两部分的结果进行可能的组合，组合出最后答案
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j,k,input[i]))
        return res

    def helper(self,num1,num2,op):
        if op == '+':
            return num1+num2
        elif op == '-':
            return num1-num2
        elif op == '*':
            return num1*num2
