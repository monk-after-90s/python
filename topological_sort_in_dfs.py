from pythonds import Stack

from dfs_knight_tour import DFSGraph


def dfsvisit(self, startVertex):
    startVertex.setColor('gray')
    self.time += 1
    startVertex.setDiscovery(self.time)
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            self.dfsvisit(nextVertex)
    startVertex.setColor('black')
    self.time += 1
    startVertex.setFinish(self.time)
    if not hasattr(self, 'topological_sort_stack'):
        self.topological_sort_stack = Stack()
    self.topological_sort_stack.push(startVertex)


DFSGraph.dfsvisit = dfsvisit

if __name__ == '__main__':
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
    g.dfs()
    # 输出topological sort
    while not g.topological_sort_stack.isEmpty():
        print(g.topological_sort_stack.pop().getId())
