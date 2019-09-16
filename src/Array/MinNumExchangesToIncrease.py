'''
给定一个序列，可以任意进行两两交换，最少用多少次，可以变成递增序列
eg:
Input:5 4 3 2 1
Output: 2(5和1交换，4和2交换)

Input:2 3 1 4
Output: 2(首先1，2交换，然后2，3交换)
思路：
关键是发现怎么交换是最快的，
比如例子1：5占了1的位置，1占了5的位置，那么彼此互换一次就可以解决
比如例子2：2占了1的位置，1占了3的位置，3占了2的位置，就需要交换两次才能解决
这种错位其实形成了一个环，k个元素环错位，就需要k-1次交换，我们可以把一个环称作循环节
那么问题的核心就是确定循环节的个数m（元素本身就在自己该在的位置上，那么自己就是一个循环节）
需要的总的交换次数就是n-m（一共n个元素，每个循环节可以节省1次操作）
'''
import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
input_list = list(map(int, line.split()))
sort_list = sorted(input_list)

#确定每个元素应该在的位置 x:index(x)
order_dict ={}
for i in range(len(sort_list)):
    order_dict[sort_list[i]]=i

#确定循环节的个数
#flag用来记录这个元素是不是已经被循环节包括了
flag = [0]*len(input_list)
loop_num = 0
#每次循环走完一个循环节
for i in range(len(input_list)):
    if flag[i] == 0:
        loop_num += 1
        j = i
        while flag[j] ==0:
            flag[j]=1
            j = order_dict[input_list[j]]
print(n-loop_num)

