from pythonds.graphs import PriorityQueue, Graph, Vertex


def dijkstra(aGraph: Graph, start: Vertex):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                      + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)


if __name__ == '__main__':
    g = Graph()
    g.addEdge('u', 'v', 2)
    g.addEdge('u', 'w', 5)
    g.addEdge('u', 'x', 1)
    g.addEdge('v', 'u', 2)
    g.addEdge('v', 'x', 2)
    g.addEdge('v', 'w', 3)
    g.addEdge('w', 'v', 3)
    g.addEdge('w', 'u', 5)
    g.addEdge('w', 'x', 3)
    g.addEdge('w', 'y', 1)
    g.addEdge('w', 'z', 5)
    g.addEdge('x', 'u', 1)
    g.addEdge('x', 'v', 2)
    g.addEdge('x', 'w', 3)
    g.addEdge('x', 'y', 1)
    g.addEdge('y', 'x', 1)
    g.addEdge('y', 'w', 1)
    g.addEdge('y', 'z', 1)
    g.addEdge('z', 'w', 5)
    g.addEdge('z', 'y', -1)
    dijkstra(g, g.getVertex('u'))
