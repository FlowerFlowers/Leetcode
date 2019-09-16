#coding=utf-8
'''
leetcode题号： 3
寻找输入的字符串的最长不重复子串的长度
eg：
Input: "abcabcbb"
Output: 3
Input: "bbbbb"
Output: 1
Input: "pwwkew"
Output: 3
思路：用一个dict存储每个字符最后出现的位置，start是当前字串的起点
如果出现重复字符就结算一次，更新最长长度
'''
import sys
    #a是输入的字符串,.strip去除前后空格
    #temp_long暂存的字符串长度
    #dict存储每个字符最后一次出现的位置
    #max_long最长的字符串长度
    #start记录开始计算的字符的位置
for line in sys.stdin:
    a = line.strip()
    temp_long = 0
    dict={}
    max_long = 0
    start = 0
    for i in range(len(a)):
        #若在start后出现过那么需要重新计数了
        if a[i] in dict and start <= dict[a[i]]:
            max_long = max(max_long,temp_long)
            start = dict[a[i]]+1
            temp_long = i-start+1
        else:
            temp_long += 1
        # 更新a[i]字符最后一次出现的位置
        dict[a[i]]=i
    #最后一次计数和max比较
    max_long = max(max_long,temp_long)
    print(max_long)
