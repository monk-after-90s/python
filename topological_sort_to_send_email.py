from pythonds import Vertex

from dfs_knight_tour import DFSGraph
from pythonds.trees import binheap

# 建立发邮件的Graph
g = DFSGraph()
g.addEdge('insert picture', 'click send button')
g.addEdge('type in to-email', 'click send button')
g.addEdge('loggin', 'click "write email"')
g.addEdge('click "write email"', 'type in to-email')
g.addEdge('click "write email"', 'type words')
g.addEdge('type words', 'click send button')
g.addEdge('click "write email"', 'type topic')
g.addEdge('click "write email"', 'insert picture')
g.addEdge('type topic', 'click send button')
# 进行dfs
g.dfs()
# 用binaryheap排序
bq = binheap.BinHeap()
# 将最大finish time 排在最前
bq.buildHeap([(-aVertex.getFinish(), aVertex) for aVertex in g])
# 输出顺序
while not bq.isEmpty():
    print(bq.delMin()[1].getId())

# g.addEdge('A', 'B', 7)
# g.addEdge('A', 'C', 5)
# g.addEdge('A', 'F', 1)
# g.addEdge('B', 'A', 2)
# g.addEdge('B', 'D', 7)
# g.addEdge('B', 'E', 3)
# g.addEdge('C', 'B', 2)
# g.addEdge('C', 'F', 8)
# g.addEdge('D', 'A', 1)
# g.addEdge('D', 'E', 2)
# g.addEdge('D', 'F', 4)
# g.addEdge('E', 'A', 6)
# g.addEdge('E', 'D', 5)
# g.addEdge('F', 'B', 1)
# g.addEdge('F', 'E', 8)
# bfs.bfs(g, g.getVertex('A'))

# g.addEdge(1, 2, 10)
# g.addEdge(1, 3, 15)
# g.addEdge(1, 6, 5)
# g.addEdge(2, 3, 7)
# g.addEdge(3, 4, 7)
# g.addEdge(3, 6, 10)
# g.addEdge(4, 5, 7)
# g.addEdge(6, 4, 5)
# g.addEdge(5, 6, 13)
# bfs.bfs(g, g.getVertex(1))
# prim(g, g.getVertex('A'))
