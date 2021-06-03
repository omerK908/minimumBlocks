
class Vertex(object):

    def __init__(self, key):
        self.path = []
        self.id = key
        self.edges = {}

    def addEdge(self, edge):
        self.edges[edge.getKey()] = edge

    def getConnections(self):
        return self.edges.keys()

    def getId(self):
        return self.id

    def getEdge(self, edgeId):
        if edgeId not in self.edges:
            return None
        return self.edges[edgeId]

    # def getWeight(self, neighbor):
    #     return self.edges[neighbor]

    def __str__(self):
        return str(self.id)

# Graph object