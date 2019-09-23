'''
leetcode题号：299
bull 代表两个字符串里位置相同并且数也相同的个数
cow 代表两个字符串里数相同的个数（减去bull）
eg：
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

思路： 循环得到bull，生成字典，两个字典都有的key，较小的values是相同的字符数
'''
from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #Counter函数计数str中每个字母出现的次数
        dict1, dict2 = Counter(secret), Counter(guess)
        cow_count = 0
        #统计相同的字符数，如果两个字典都有的字符，取小的
        for key in dict1:
            if key in dict2:
                cow_count += min(dict1[key],dict2[key])
        bull_count = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull_count +=1
        return '%sA%sB' % (bull_count,cow_count-bull_count)
