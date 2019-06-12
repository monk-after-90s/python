# from Three_missionaries_and_three_cannibals_problem import recursive
# 用一个tuple表示前后岸的情况，((missionaries,cannibals),(missionaries,cannibals),Fasle)
# 力求求出所有无重复的方案
# 5种运输方案
# 1、运输了一个传教士 # 2、运输了一个食人族 # 3、运输了两个传教士# 4、运输了两个食人族 5、运输一个传教士和食人族
# 重写Vertex
from pythonds import Vertex, Queue


class Bank_state(Vertex):
    def __init__(self, id, missionaries_num: int = 3, cannibals_num: int = 3):
        super(Bank_state, self).__init__(id)
        # 河岸状态
        self.state = ((missionaries_num, cannibals_num), (0, 0), False)  # False表示船在前岸，True表示船在后岸

    # 5种运输方案
    def next_state(self, n: int):
        # # 如果跟前一个运输一样，没有意义
        # if n == self.getId():
        #     return
        new_state = Bank_state(n, 0, 0)
        # 运输一个传教士
        if n == 0:
            # 船在前岸,且前岸至少有一个传教士
            if (not self.state[2]) and self.state[0][0] >= 1:
                # 计算运输后的状态
                new_state.state = (
                    (self.state[0][0] - 1, self.state[0][1]), (self.state[1][0] + 1, self.state[1][1]), True)
            # 船在后岸且后岸至少有一个传教士
            elif self.state[2] and self.state[1][0] >= 1:
                new_state.state = (
                    (self.state[0][0] + 1, self.state[0][1]), (self.state[1][0] - 1, self.state[1][1]), False)
        # 运输了一个食人族
        elif n == 1:
            # 船在前岸，且至少有一个食人族
            if (not self.state[2]) and self.state[0][1] >= 1:
                # 计算运输后的状态
                new_state.state = (
                    (self.state[0][0], self.state[0][1] - 1), (self.state[1][0], self.state[1][1] + 1), True)
            # 船在后岸，且至少有一个食人族
            elif self.state[2] and self.state[1][1] >= 1:
                new_state.state = (
                    (self.state[0][0], self.state[0][1] + 1), (self.state[1][0], self.state[1][1] - 1), False)
        # 运输了两个传教士
        elif n == 2:
            # 船在前岸且至少有两个传教士
            if (not self.state[2]) and self.state[0][0] >= 2:
                # 计算运输后的状态
                new_state.state = (
                    (self.state[0][0] - 2, self.state[0][1]), (self.state[1][0] + 2, self.state[1][1]), True)
            # 船在后岸且至少有两个传教士
            elif self.state[2] and self.state[1][0] >= 2:
                new_state.state = (
                    (self.state[0][0] + 2, self.state[0][1]), (self.state[1][0] - 2, self.state[1][1]), False)
        # 运输了两个食人族
        elif n == 3:
            # 船在前岸且至少有两个食人族
            if (not self.state[2]) and self.state[0][1] >= 2:
                # 计算运输后的状态
                new_state.state = (
                    (self.state[0][0], self.state[0][1] - 2), (self.state[1][0], self.state[1][1] + 2), True)
            # 船在后岸且至少有两个食人族
            elif self.state[2] and self.state[1][1] >= 2:
                new_state.state = (
                    (self.state[0][0], self.state[0][1] + 2), (self.state[1][0], self.state[1][1] - 2), False)
        # 运输一个传教士和食人族
        elif n == 4:
            # 船在前岸且至少有一个食人族和至少一个传教士
            if (not self.state[2]) and self.state[0][1] >= 1 and self.state[0][0] >= 1:
                new_state.state = (
                    (self.state[0][0] - 1, self.state[0][1] - 1), (self.state[1][0] + 1, self.state[1][1] + 1), True)
            # 船在后岸且至少有一个食人族和至少一个传教士
            elif self.state[2] and self.state[1][0] >= 1 and self.state[1][1] >= 1:
                new_state.state = (
                    (self.state[0][0] + 1, self.state[0][1] + 1), (self.state[1][0] - 1, self.state[1][1] - 1), False)
        return new_state if new_state.state != ((0, 0), (0, 0), False) else None

    def bfs_transport(self):
        goal_vertex = []  # 存储达到目的状态的节点
        history = []  # 存储历史状态的列表
        self.setDistance(0)
        self.setPred(None)
        vertQueue = Queue()
        vertQueue.enqueue(self)
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            # 检查是否到达目的状态
            if currentVert.state == (self.state[1], self.state[0], True):
                goal_vertex.append(currentVert)
                continue
            else:
                # 检查历史记录
                if currentVert.state in history:
                    continue
                # 检查是否发生悲剧
                elif 0 < currentVert.state[0][0] < currentVert.state[0][1] or 0 < currentVert.state[1][0] < \
                        currentVert.state[1][1]:
                    continue
                else:
                    history.append(currentVert.state)
            # 创建下一可能状态
            for i in range(5):
                # 如果跟前一个运输一样，没有意义
                if i != currentVert.getId():
                    nbr = currentVert.next_state(i)
                    if nbr:
                        currentVert.addNeighbor(nbr)

            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')
        # 输出结果
        # 文字描述
        words = {0: '运输一个传教士', 1: '运输一个食人族 ', 2: '运输两个传教士', 3: '运输两个食人族', 4: '运输一个传教士和食人族'}
        programs = ''
        n = 0
        for agoal in goal_vertex:
            cur_vertex = agoal
            # 新方案
            if cur_vertex != self:
                n += 1
                programs += '方案' + str(n) + ':\n'
            program = '\n\n'
            while cur_vertex != self:
                program = words[cur_vertex.getId()] + '\n' + program
                cur_vertex = cur_vertex.getPred()
            programs += program
        return programs

    # def dfs_transport(self, history=[]):
    #     # goal_vertex = []  # 存储达到目的状态的节点
    #     # 检查是否到达目的状态
    #     if self.state == ((0, 0), self.state[1], True):
    #         return [self]
    #     else:
    #         # 检查历史记录
    #         if self.state in history:
    #             return
    #             # 检查是否发生悲剧
    #         elif 0 < self.state[0][0] < self.state[0][1] or 0 < self.state[1][0] < \
    #                 self.state[1][1]:
    #             return
    #         else:
    #             history.append(self.state)
    #
    #     # 创建下一可能状态
    #     for i in range(5):
    #         # 如果跟前一个运输一样，没有意义
    #         if i != self.getId():
    #             nbr = self.next_state(i)
    #             if nbr:
    #                 self.addNeighbor(nbr)
    #     for nextVertex in self.getConnections():
    #         nextVertex.setPred(self)
    #         next_trans = self.dfs_transport(nextVertex, history)
    #         if next_trans

    def dfs_transport(self, history=[]):
        # goal_vertex = []  # 存储达到目的状态的节点

        # 文字描述
        words = {0: '运输一个传教士', 1: '运输一个食人族 ', 2: '运输两个传教士', 3: '运输两个食人族', 4: '运输一个传教士和食人族'}
        # 检查是否到达目的状态
        if self.state == ((0, 0), self.state[1], True):
            return [words[self.getId()] + '\n']
        else:
            # 检查历史记录
            if self.state in history:
                return []
                # 检查是否发生悲剧
            elif 0 < self.state[0][0] < self.state[0][1] or 0 < self.state[1][0] < \
                    self.state[1][1]:
                return []
            else:
                history.append(self.state)

        # 创建下一可能状态
        for i in range(5):
            # 如果跟前一个运输一样，没有意义
            if i != self.getId():
                nbr = self.next_state(i)
                if nbr:
                    self.addNeighbor(nbr)
        # 函数返回值
        programs = []
        for nextVertex in self.getConnections():
            nextVertex.setPred(self)
            next_trans = nextVertex.dfs_transport(history)
            if next_trans and len(next_trans):
                programs += [words.get(self.getId(), '') + '\n' + next_tran for next_tran in next_trans]
        if len(programs) > 0:
            # 最外递归
            if self.state[1] == (0, 0) and self.state[2] == False:
                # 文字描述
                literal = ''
                n = 0
                for program in programs:
                    n += 1
                    literal += '方案' + str(n) + ':' + program
                return literal
            else:
                return programs


if __name__ == '__main__':
    print(Bank_state('', 4, 2).dfs_transport())
