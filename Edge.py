def makeKey(nodeFrom, nodeTo):
    return str(nodeFrom.getId()) + "-" + str(nodeTo.getId())


class Edge(object):

    def __init__(self, src_vertex, dst_vertex):
        self.key = dst_vertex.getId()
        self.src = src_vertex
        self.dst = dst_vertex



    # def getConnections(self):
    #     return self.connectedTo.keys()

    def getSrcNode(self):
        return self.src

    def getDstNode(self):
        return self.dst

    def getKey(self):
        return self.key


    def __str__(self):
        return str(str(self.getSrcNode().getId()) + "-" + str(self.key))



# Graph object