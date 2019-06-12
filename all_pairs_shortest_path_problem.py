from pythonds import Graph, Vertex

import bfs

# 构建Graph
g = Graph()
g.addEdge('A', 'C')
g.addEdge('A', 'B')
g.addEdge('C', 'E')
g.addEdge('C', 'D')
g.addEdge('B', 'A')
g.addEdge('B', 'D')
g.addEdge('D', 'B')
g.addEdge('E', 'D')

# 保存all pairs shortest path结果的字典
res = {}
for aVertex in g:
    # 从一个节点进行bfs
    bfs.bfs(g, aVertex)
    # 统计其他节点到这个节点的距离
    res[aVertex.getId()] = {}
    for otherVert in g:
        if not (otherVert is aVertex):
            # 存储距离
            res[aVertex.getId()][otherVert.getId()] = otherVert.getDistance()
            # 恢复所有节点为白色
            otherVert.setColor('white')
    aVertex.setColor('white')
