from knight_tour import DFSGraph, Vertex


def transposition_graph(self: DFSGraph):
    # 新建DFSGraph对象
    t_graph = DFSGraph()
    # 拷贝节点
    for aVertex in self:
        # 检查是否已经存储
        if aVertex.getId() not in t_graph.getVertices():
            t_graph.addVertex(aVertex.getId())
        # 建立反向节点
        for nbr in aVertex.getConnections():
            t_graph.addEdge(nbr.getId(), aVertex.getId())
    return t_graph


def SCC_keys(self: DFSGraph):
    t_graph: DFSGraph = self.transposition_graph()
    self.dfs()
    # 记录scc 树的keys
    scc_keys = ''
    # transposition graph 的DFS
    for aVertex in t_graph:
        aVertex.setColor('white')
        aVertex.setPred(-1)
    # 根据原始Graph 节点finish time倒序排列确定key的顺序
    org_vetices = list(self)
    org_vetices.sort(key=lambda x: x.getFinish(), reverse=True)
    for aVertex in org_vetices:
        current_vertex = t_graph.getVertex(aVertex.getId())
        if current_vertex.getColor() == 'white':
            scc_keys += str(t_graph.dfsvisit(current_vertex)) + '\n'
    return scc_keys


# def SCC(self: DFSGraph):
#     # 封装各个计算SCC的各个过程
#     #     transposition GRAPH
#     t_graph = self.transposition_graph()
#     # DFS
#     self.dfs()
#     self.transposition_dfs(t_graph)
#     #   输出SCC信息


DFSGraph.transposition_graph = transposition_graph
DFSGraph.SCC_keys = SCC_keys

if __name__ == '__main__':
    # 建立图
    org_graph = DFSGraph()
    org_graph.addEdge('A', 'B')
    org_graph.addEdge('E', 'A')
    org_graph.addEdge('B', 'C')
    org_graph.addEdge('B', 'E')
    org_graph.addEdge('C', 'C')
    org_graph.addEdge('C', 'F')
    org_graph.addEdge('D', 'B')
    org_graph.addEdge('D', 'G')
    org_graph.addEdge('E', 'D')
    org_graph.addEdge('F', 'H')
    org_graph.addEdge('G', 'E')
    org_graph.addEdge('H', 'I')
    org_graph.addEdge('I', 'F')
    print(org_graph.SCC_keys())
