import re

import Graph


class MinimumBlocks(object):

    def __init__(self, str_a, str_b):

        if self.is_good(str_a, str_b):
            self.str_a = str_a
            self.str_b = str_b
            self.hash_subs_counter = {}
            self.init_dict_for_BFS()  # O(n * (2^n))
        else:
            raise Exception("string doesnt match")

    def init_graph(self, graph):
        for _ in range(len(self.str_a) + 1):
            graph.addVertex()

        for ID in range(0, len(self.str_a)):
            graph.addEdge(ID, ID + 1)

    def get_substring(self, edge):
        if edge is None:
            print("get_substring: edge is None")
        return self.str_a[edge.getSrcNode().getId(): edge.getDstNode().getId()]

    def substrings(self, string):
        # returns all the substrings of string
        res = [string[i: j] for i in range(len(string))
               for j in range(i + 1, len(string) + 1)]
        return res

    def make_graph_by_substrings(self, substrings_list):
        # add edges by the substrings of str_b on the linear graph of str_a
        ans_graph = Graph.Graph()
        self.init_graph(ans_graph)  # init graph by str_a
        # add edges by perm of str_b
        for substring in substrings_list: #2^n
            size = len(substring)
            if size > 1:  # because all substring of len 1 already connected in the graph
                matches = re.finditer(substring, self.str_a) #n
                matches_positions = [match.start() for match in matches]
                counter = self.hash_subs_counter[substring]

                for idx in matches_positions: #n
                    if counter > 0 and ans_graph.getEdge(idx, idx + size) is None:
                        ans_graph.addEdge(idx, idx + size)
                    elif counter == 0:
                        break
                    counter -= 1
        return ans_graph

    def get_substrings_from_bfs(self, list_of_bfs):
        # the bfs returns the id's of the vertexes,
        # this function returns the substrings between the vertexes
        ans = []
        for graph in list_of_bfs:
            tmp_list = []
            src = graph.pop(0)
            while graph:
                dst = graph.pop(0)
                tmp_list.append(self.str_a[src:dst])
                src = dst
            ans.append(tmp_list)
        return ans

    def BFS(self, s, goal_id): #n choose 2 = n ^ 2
        # s: the start vertex, goal_id: the id of the last vertex
        llist = []
        list_hashMap = {}
        llist.append(s)
        list_hashMap[s.getId()] = s
        closeList = {}
        while llist:
            vertexSrc = llist.pop(0)
            closeList[vertexSrc.getId()] = vertexSrc
            for edgeId in vertexSrc.edges:
                #get the vertex at the end of the edge
                edge = vertexSrc.edges[edgeId]
                vertexDst = edge.getDstNode()
                if not vertexDst.visited:
                    vertexDst.path = vertexSrc.path.copy()
                    vertexDst.path.append(vertexSrc.getId())
                    vertexDst.visited = True
                if vertexDst.getId() not in closeList and vertexDst.getId() not in list_hashMap:
                    if vertexDst.getId() == goal_id:
                        vertexDst.path.append(vertexDst.getId())
                        return vertexDst.path
                    llist.append(vertexDst)
                    list_hashMap[vertexDst.getId()] = vertexDst

        return None

    def run(self):

        g1 = self.make_graph_by_substrings(self.substrings(self.str_b)) #O(n * 2^n)
        bfs_g1 = [self.BFS(g1.getVertex(0), len(self.str_a))]

        return self.get_substrings_from_bfs(bfs_g1)

    # init dict of minimun number of edges to each substring
    def init_dict_for_BFS(self): # O(n * (2^n))
        subs_b = self.substrings(self.str_b)
        for substring in subs_b:  #2^n
            matches_of_b_in_a = re.finditer(substring, self.str_a)  #n
            matches_positions_b_in_a = [match.start() for match in matches_of_b_in_a]

            matches_of_a_in_b = re.finditer(substring, self.str_b)
            matches_positions_a_in_b = [match.start() for match in matches_of_a_in_b]

            self.hash_subs_counter[substring] = min(len(matches_positions_b_in_a), len(matches_positions_a_in_b))

    def is_good(self, str_a, str_b):
        return len(str_a) == len(str_b) and sorted(str_a) == sorted(str_b)

