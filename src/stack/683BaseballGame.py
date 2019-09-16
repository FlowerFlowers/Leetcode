'''
leetcode编号：683
一个List(str)里的数如果是
1。Integer (one round's score): Directly represents the number of points you get in this round.
2。"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
3。"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
4。"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
eg:
Input: ["5","2","C","D","+"]
Output: 30
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.

思路：栈
易错点：判断整数不能用.isdigit（）,因为可能是负整数
'''
from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        sum = 0
        for i in range(len(ops)):
            if ops[i].isdigit() or ops[i][0] == '-':
                sum +=int(ops[i])
                stack.append(ops[i])
            elif ops[i]== '+':
                temp = int(stack[-1])+int(stack[-2])
                stack.append(temp)
                sum += temp
            elif ops[i] == 'C':
                temp = int(stack[-1])
                stack.pop()
                sum -= temp
            elif ops[i] == 'D':
                temp = 2*int(stack[-1])
                stack.append(temp)
                sum +=temp
        return sum

s=Solution()
print(s.calPoints(["-21","-66","39","+","+"]))