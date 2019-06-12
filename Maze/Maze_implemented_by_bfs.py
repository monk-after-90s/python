from pythonds import Graph

import bfs

text = []  # 存储迷宫数据的列表
with open('maze2.txt', 'r') as f:
    for line in f:
        text.append(line[:-1])
start = -1  # 起点ID
# 终点ID
end = []
# 构建Graph
g = Graph()
for row in range(len(text)):
    for col in range(len(text[0])):
        # 将' '和‘S存储为节点
        if text[row][col] == ' ' or text[row][col] == 'S':
            # 计算ID
            id = row * len(text[0]) + col
            # 找到起点
            if text[row][col] == 'S':
                start = id
            # 找到一个终点
            if row == 0 or row == len(text) - 1 or col == 0 or col == len(text[0]) - 1:
                end.append(id)

            # 计算四周ID
            # 上
            if row - 1 >= 0 and (text[row - 1][col] == ' ' or text[row - 1][col] == 'S'):
                nbr_id = (row - 1) * len(text[0]) + col
                g.addEdge(id, nbr_id)
            # 下
            if row + 1 < len(text) and (text[row + 1][col] == ' ' or text[row + 1][col] == 'S'):
                nbr_id = (row + 1) * len(text[0]) + col
                g.addEdge(id, nbr_id)
            # 左
            if col - 1 >= 0 and (text[row][col - 1] == ' ' or text[row][col - 1] == 'S'):
                nbr_id = row * len(text[0]) + (col - 1)
                g.addEdge(id, nbr_id)
            # 右
            if col + 1 < len(text[0]) and (text[row][col + 1] == ' ' or text[row][col + 1] == 'S'):
                nbr_id = row * len(text[0]) + (col + 1)
                g.addEdge(id, nbr_id)
# bfs
bfs.bfs(g, g.getVertex(start))
# 输出起点到各终点的路径
for anend in end:
    print('到终点{},{}的路径:'.format(anend // len(text[0]), anend % len(text[0])))
    # 存储路径节点
    path = []
    cur_vertex = g.getVertex(anend)
    while cur_vertex != g.getVertex(start):
        path.append(cur_vertex)
        cur_vertex = cur_vertex.getPred()
    # 打印矩阵
    for row in range(len(text)):
        for col in range(len(text[0])):
            if g.getVertex(row * len(text[0]) + col) in path:
                print(1, sep="", end='')
            else:
                print(text[row][col], sep="", end='')
        print('\n')
