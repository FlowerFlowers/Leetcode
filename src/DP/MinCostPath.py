'''
给一个n*m的矩阵，选择从左上走到右下的最小代价
2
3
9 8 6
2 3 7
输出为21 ：9-2-3-7

'''
import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
weight = []
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    weight.append(values)

min_weight = [[0 for i in range(m)] for j in range(n)]
min_weight[0][0] = weight[0][0]
for i in range(1,m):
    min_weight[0][i] =min_weight[0][i-1]+weight[0][i]
for i in range(1,n):
    min_weight[i][0] = min_weight[i-1][0]+weight[i][0]

for i in range(1,n):
    for j in range(1,m):
        min_weight[i][j] = min(min_weight[i-1][j],min_weight[i][j-1])+weight[i][j]
print(min_weight)
print(min_weight[n-1][m-1])
'''
2
3
9 8 6
2 3 7
'''