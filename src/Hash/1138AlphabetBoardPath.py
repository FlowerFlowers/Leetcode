'''
leetcode 编号：1138
给了一个字母表
a b c d e
f g h i j
k l m n o
p q r s t
u v w x y
z

从''a'用最小的步数走到target
u: up d :down r: right l: left !:到达
eg
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

思路：分别计算初始位置和结束位置的横纵坐标，然后决定走的距离
易错点：往下和往右可能走出去（'z'的存在），所以先往上，往左走

'''
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        temp = 'a'
        res = ''
        for i in range(len(target)):
            pre_divided = ord(temp)-ord('a')
            pre_quotient = pre_divided//5
            divided = ord(target[i])-ord('a')
            quotient = divided//5
            down = quotient - pre_quotient
            pre_rem = (ord(temp) - ord('a')) % 5
            rem = (ord(target[i])-ord('a')) % 5
            right = rem-pre_rem
            if right < 0:
                left = abs(right)
                res += 'L' * left
            if down < 0:
                up = abs(down)
                res += 'U'*up
            if down > 0:
                res += 'D'*down
            if right > 0:
                res += 'R'*right
            res += '!'
            temp = target[i]
        return res


s = Solution()
print(s.alphabetBoardPath('code'))
