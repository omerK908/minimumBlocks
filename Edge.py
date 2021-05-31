def makeKey(nodeFrom, nodeTo):
    return str(nodeFrom.getId()) + "-" + str(nodeTo.getId())


class Edge(object):

    def __init__(self, src_vertex, dst_vertex, weight=0):
        self.weight = weight
        self.key = dst_vertex.getId()
        self.src = src_vertex
        self.dst = dst_vertex

    # def addNeighbor(self, neighbor, weight=0):
    #     self.connectedTo[neighbor] = weight

    # def getConnections(self):
    #     return self.connectedTo.keys()

    def getSrcNode(self):
        return self.src

    def getDstNode(self):
        return self.dst

    def getKey(self):
        return self.key

    def getWeight(self, neighbor):
        return self.weight

    def __str__(self):
        return str(self.key)



# Graph object