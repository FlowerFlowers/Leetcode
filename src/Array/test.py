import sys

if __name__ == "__main__":
    # 读取第一行的n 记录每n个最多出一张图,strip去除首位空格
    n = int(sys.stdin.readline().strip())
    # 读取第二行的m 记录待处理的推荐结果数
    m = int(sys.stdin.readline().strip())
    # temp用来记录距离上一个图片后前面有多少个视频了
    temp = 0
    temp_list = []
    # 记录是不是第一次见到图片
    flag_first = 1
    for i in range(m):
        # 读取每一行
        line = str(sys.stdin.readline().strip())
        # flag记录上图片还是视频
        flag = line[0]
        if flag == 'V':
            print(line)
            temp += 1
        else:
            # 如果是第一次见到图片，直接输出
            if flag_first == 1:
                print(line)
                temp = 0
                flag_first = 0
            # 如果是图片就加入list
            else:
                temp_list.append(line)
    # 如果积攒了足够的视频，就尝试从图片list输出
        if temp >= (n-1):
            if len(temp_list) != 0:
                print(temp_list[0])
                temp_list.pop(0)
                temp = 0

