import sys
from pythonds.graphs import PriorityQueue, Graph, Vertex


def prim(G: Graph, start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)


if __name__ == '__main__':
    g = Graph()
    g.addEdge('A', 'B', 2)
    g.addEdge('A', 'C', 3)
    g.addEdge('B', 'A', 2)
    g.addEdge('B', 'C', 1)
    g.addEdge('B', 'E', 4)
    g.addEdge('B', 'D', 1)
    g.addEdge('C', 'A', 3)
    g.addEdge('C', 'B', 1)
    g.addEdge('C', 'F', 5)
    g.addEdge('D', 'B', 1)
    g.addEdge('D', 'E', 1)
    g.addEdge('E', 'D', 1)
    g.addEdge('E', 'B', 4)
    g.addEdge('E', 'F', 1)
    g.addEdge('F', 'C', 5)
    g.addEdge('F', 'E', 1)
    g.addEdge('F', 'G', 1)
    g.addEdge('G', 'F', 1)
    prim(g, g.getVertex('A'))
