import copy

from pythonds import Graph, Vertex, Queue


# 重写Vertex，将两个水壶的状态保存进去
class Jug_operation(Vertex):
    def __init__(self, id):
        super(Jug_operation, self).__init__(id)
        jugs_state = [0, 0]


def jug_problem_bfs(start_id, goal: list, jug_a=4, jug_b=3, memo: list = []):  # memo用来记录走过的经历，用来避免重复计算
    start = Jug_operation(start_id)
    # 构建6个操作
    op = ['->A', '->B', 'A->',
          'B->', 'A->B', 'B->A']
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert: Jug_operation = vertQueue.dequeue()
        # 更新当前水壶状态
        # 先复制前驱结点状态
        if currentVert.getPred() == None:
            currentVert.jugs_state = [0, 0]
        else:
            currentVert.jugs_state = copy.copy(currentVert.getPred().jugs_state)
        # 根据6种操作进行计算
        if currentVert.getId() == op[0]:
            currentVert.jugs_state[0] = jug_a
        elif currentVert.getId() == op[1]:
            currentVert.jugs_state[1] = jug_b
        elif currentVert.getId() == op[2]:
            currentVert.jugs_state[0] = 0
        elif currentVert.getId() == op[3]:
            currentVert.jugs_state[1] = 0
        elif currentVert.getId() == op[4]:
            # A壶有水,B壶可以接收
            if currentVert.jugs_state[0] > 0 and 0 <= currentVert.jugs_state[1] < jug_b:
                trans_water = min(jug_b - currentVert.jugs_state[1], currentVert.jugs_state[0])
                currentVert.jugs_state[0] -= trans_water
                currentVert.jugs_state[1] += trans_water
        elif currentVert.getId() == op[5]:
            # B壶有水，A壶可以接收
            if currentVert.jugs_state[1] > 0 and 0 <= currentVert.jugs_state[0] < jug_a:
                trans_water = min(currentVert.jugs_state[1], jug_a - currentVert.jugs_state[0])
                currentVert.jugs_state[1] -= trans_water
                currentVert.jugs_state[0] += trans_water
        # 检查是否达到目标
        if currentVert.jugs_state == goal:
            # 输出过程
            res = ''
            while True:
                res = currentVert.getId() + '\n' + res
                if currentVert.getPred() != None:
                    currentVert = currentVert.getPred()
                else:
                    break
            return res
        else:
            # 检查是否计算过当前状态
            if currentVert.jugs_state in memo:
                continue
            else:
                memo.append(currentVert.jugs_state)
        # 连接新的下级节点
        for id in op:
            if id != currentVert.getId():
                currentVert.addNeighbor(Jug_operation(id))

        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


if __name__ == '__main__':
    res = ''
    # 尝试所有可能的开始
    for start in ['->A', '->B', 'A->',
                  'B->', 'A->B', 'B->A']:
        res = jug_problem_bfs(start, goal=[4, 0], jug_a=5, jug_b=3)
        if res != None:
            print(res, end='\n\n')

    # def jug_problem_bfs(g: Graph, start: Jug_operation):
#     start.setDistance(0)
#     start.setPred(None)
#     vertQueue = Queue()
#     vertQueue.enqueue(start)
#     while (vertQueue.size() > 0):
#         currentVert = vertQueue.dequeue()
#         for nbr in currentVert.getConnections():
#             # if (nbr.getColor() == 'white'):
#             # nbr.setColor('gray')
#             nbr.setDistance(currentVert.getDistance() + 1)
#             nbr.setPred(currentVert)
#             vertQueue.enqueue(nbr)
#             #计算新的水壶状态
#             if
#         # currentVert.setColor('black')


# # 重写Graph
# class Jugs_operations(Graph):
#     def addEdge(self, f: Jug_operation, t: Jug_operation, cost=0):
#         f.addNeighbor(t, cost)

# for aVertex in op:
#     for another_ver in op:
#         if aVertex != another_ver:
#             aVertex.addNeighbor(another_ver)
