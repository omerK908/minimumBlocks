import Minimun_Blocks


def makeGraph():

    mb = Minimun_Blocks.MinimumBlocks("babcbcab", "acbbabcb")
    # a = 0
    # b = 9
    # mb.graph.addEdge(a, b)
    # vertex_a = mb.graph.getVertex(a)
    # vertex_b = mb.graph.getVertex(b)
    #
    # edge5 = mb.graph.getEdge(vertex_a.getId(), vertex_b.getId())
    # print(mb.get_substring(edge5))
    # print(str(mb.partitions("abc")))

    # str_a = "doredlich"
    #
    # str_b = "edlichdor"
    #
    # g = Graph.Graph()
    # for _ in range(len(str_a) + 1):
    #     g.addVertex()
    #
    # for id in range(0, len(str_a)):
    #     g.addEdge(id, id + 1)
    #
    # a = 0
    # b = 9
    # g.addEdge(a, b)
    # vertex_a = g.getVertex(a)
    # vertex_b = g.getVertex(b)
    #
    # edge5 = g.getEdge(vertex_a.getId(), vertex_b.getId())
    # if edge5 == None:
    #     print("no edge")
    # else:
    #     print(str_a[vertex_a.getId(): edge5.getKey()])
    #     # print(vertex_a.getId(), edge5.getKey())


if __name__ == '__main__':
    makeGraph()


