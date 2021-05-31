import Vertex
import Edge


class Graph(object):

    def __init__(self):
        self.vertexes = {}
        self.totalNum = 0

    def addVertex(self):
        newVertex = Vertex.Vertex(self.totalNum)
        self.vertexes[self.totalNum] = newVertex
        self.totalNum += 1
        return newVertex

    def getVertex(self, vertex_id):
        if vertex_id in self.vertexes:
            return self.vertexes[vertex_id]
        else:
            return None

    def addEdge(self, from_vertex_id, to_vertex_id, weight=0):
        if from_vertex_id not in self.vertexes:
            print("from_vertex_id not in vertexes")
            return
        if to_vertex_id not in self.vertexes:
            print(str(to_vertex_id) + " not in vertexes")
            return
        edge = Edge.Edge(self.vertexes[from_vertex_id], self.vertexes[to_vertex_id])
        self.vertexes[from_vertex_id].addEdge(edge)

    def getVertices(self):
        return self.vertexes.keys()

    def __iter__(self):
        # this sepcial function allows us to iterate through master list
        return iter(self.vertexes.values())

    def __contains__(self, vertex_id):
        # this special function allows us to use IN operator
        if vertex_id in self.vertexes:
            return True
        else:
            return False

    def getEdge(self, key_src, key_dst):
        srcVertex = self.getVertex(key_src)
        edge = srcVertex.getEdge(key_dst)
        if edge == None:
            print("getEdge(self," + str(key_src) + ", " + str(key_dst) + "): return None")
        return edge




