import copy

# from pythonds import Vertex

# import dfs_knight_tour

# 重写Vertex，将两个水壶的状态保存进去
# class Jug_operation(Vertex):
#     def __init__(self, id):
#         super(Jug_operation, self).__init__(id)
#         jugs_state = [0, 0]
from dfs_knight_tour import DFSGraph
from two_jugs_problem.two_jugs_get_water_bfs import Jug_operation


def jug_problem_dfsvisit(self, start, goal: list, jug_a=4, jug_b=3, memo: list = []):  # memo用来记录走过的经历，用来避免重复计算
    # 构建6个操作
    op = ['->A', '->B', 'A->',
          'B->', 'A->B', 'B->A']
    startVertex = start if isinstance(start, Jug_operation) else Jug_operation(start)
    startVertex.setColor('gray')
    self.time += 1
    startVertex.setDiscovery(self.time)
    # 更新当前水壶状态
    # 先复制前驱结点状态
    if startVertex.getPred() == None:
        startVertex.jugs_state = [0, 0]
    else:
        startVertex.jugs_state = copy.copy(startVertex.getPred().jugs_state)
    # 根据6种操作进行计算
    if startVertex.getId() == op[0]:
        startVertex.jugs_state[0] = jug_a
    elif startVertex.getId() == op[1]:
        startVertex.jugs_state[1] = jug_b
    elif startVertex.getId() == op[2]:
        startVertex.jugs_state[0] = 0
    elif startVertex.getId() == op[3]:
        startVertex.jugs_state[1] = 0
    elif startVertex.getId() == op[4]:
        # A壶有水,B壶可以接收
        if startVertex.jugs_state[0] > 0 and 0 <= startVertex.jugs_state[1] < jug_b:
            trans_water = min(jug_b - startVertex.jugs_state[1], startVertex.jugs_state[0])
            startVertex.jugs_state[0] -= trans_water
            startVertex.jugs_state[1] += trans_water
    elif startVertex.getId() == op[5]:
        # B壶有水，A壶可以接收
        if startVertex.jugs_state[1] > 0 and 0 <= startVertex.jugs_state[0] < jug_a:
            trans_water = min(startVertex.jugs_state[1], jug_a - startVertex.jugs_state[0])
            startVertex.jugs_state[1] -= trans_water
            startVertex.jugs_state[0] += trans_water
            # 检查是否达到目标
    if startVertex.jugs_state == goal:
        # 输出过程
        res = ''
        while True:
            res = startVertex.getId() + '\n' + res
            if startVertex.getPred() != None:
                startVertex = startVertex.getPred()
            else:
                break
        return res
    else:
        # 检查是否计算过当前状态
        if startVertex.jugs_state in memo:
            return
        else:
            memo.append(startVertex.jugs_state)

    # 连接新的下级节点
    for id in op:
        if id != startVertex.getId():
            startVertex.addNeighbor(Jug_operation(id))

    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            res = self.jug_problem_dfsvisit(nextVertex, goal=goal, jug_a=jug_a, jug_b=jug_b, memo=memo)
            if res != None:
                return res
    startVertex.setColor('black')
    self.time += 1
    startVertex.setFinish(self.time)


DFSGraph.jug_problem_dfsvisit = jug_problem_dfsvisit
if __name__ == '__main__':
    # 尝试所有可能的开始
    for start in ['->A', '->B']:
        res = DFSGraph().jug_problem_dfsvisit(start, goal=[2, 0], jug_a=4, jug_b=3)
        if res != None:
            print(res, end='\n\n')
