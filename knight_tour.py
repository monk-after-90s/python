from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_size):
    return (row * board_size) + column


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and \
                legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


def average_branching_factor(board_num: int):
    total = 0
    # 骑士可能的移动位置
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    if board_num <= 4:
        # 便览每个点
        for colum in range(board_num):
            for row in range(board_num):
                # 检查每个点的可能移动位置
                for step in moveOffsets:
                    # 检查合法位置
                    if legalCoord(colum + step[0], board_num) and legalCoord(row + step(1)):
                        # 统计
                        total += 1
    # 边长超过4,除了最外两层壳之外其余节点可移动位置全是8
    else:
        # 先计算两层外壳
        # 四角各4方块共12*4
        total += 48
        # 两层壳剩余部分
        total += (board_num - 4) * 4 * 10
        # 全图剩余部分
        total += (board_num - 4) ** 2 * 8
    return round(total / (board_num ** 2), 2)


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex: Vertex):
        scc_keys = str(startVertex.getId())  # 记录scc中节点的keys
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                scc_keys += ' ' + str(self.dfsvisit(nextVertex))
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
        return scc_keys

    # def dfsvisit(self, startVertex):
    #     startVertex.setColor('gray')
    #     self.time += 1
    #     startVertex.setDiscovery(self.time)
    #     for nextVertex in startVertex.getConnections():
    #         if nextVertex.getColor() == 'white':
    #             nextVertex.setPred(startVertex)
    #             self.dfsvisit(nextVertex)
    #     startVertex.setColor('black')
    #     self.time += 1
    #     startVertex.setFinish(self.time)

    def bfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.bfsvisit(aVertex)

    def bfsvisit(self, startVertex: Vertex):
        vertQueue = Queue()
        # 初始化开始节点
        startVertex.setColor('white')
        startVertex.setDistance(0)
        vertQueue.enqueue(startVertex)
        startVertex.setPred(None)
        while (vertQueue.size() > 0):
            # 提取单节点处理颜色
            currentVert = vertQueue.dequeue()
            if currentVert.getColor() == 'white':
                currentVert.setColor('gray')
                startVertex.setDiscovery(self.time)
                self.time += 1
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    # nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')
            startVertex.setFinish(self.time)
            self.time += 1

        # startVertex.setPred(None)


if __name__ == '__main__':
    print(average_branching_factor(6))
