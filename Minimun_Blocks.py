import re

import Graph


class MinimumBlocks(object):

    def __init__(self, str_a, str_b):
        if self.is_good(str_a, str_b):
            self.str_a = str_a
            self.str_b = str_b
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
        for substring in substrings_list:
            size = len(substring)
            if size > 1:  # because all substring of len 1 already connected in the graph
                matches = re.finditer(substring, self.str_a)
                matches_positions = [match.start() for match in matches]
                for idx in matches_positions:
                    if ans_graph.getEdge(idx, idx + size) is None:
                        ans_graph.addEdge(idx, idx + size)
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

    def BFS(self, s, goal_id):
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
        # list_of_bfs = self.get_all_bfs_path()
        # print(self.get_substrings_from_bfs(list_of_bfs))

        g1 = self.make_graph_by_substrings(self.substrings(self.str_b))
        bfs_g1 = [self.BFS(g1.getVertex(0), len(self.str_a))]
        # g2 = self.make_graph_by_substrings(self.substrings(self.str_a))
        # bfs_g2 = [self.BFS(g2.getVertex(0), len(self.str_b))]
        #
        # set_1 = set(bfs_g1)
        # set_2 = set(bfs_g2)
        #
        # list_2_items_not_in_list_1 = list(set_2 - set_1)
        # combined_bfs = bfs_g1 + list_2_items_not_in_list_1

        return self.get_substrings_from_bfs(bfs_g1)

    # def make_edges_by_permutations(self):
    #     perm_of_str_b = self.partitions(self.str_b)
    #     for lst in perm_of_str_b:
    #         # print(lst)
    #         for substring in lst:
    #             size = len(substring)
    #             if size > 1:  # because all substring of len 1 already connected in the graph
    #                 matches = re.finditer(substring, self.str_a)
    #                 matches_positions = [match.start() for match in matches]
    #                 for idx in matches_positions:
    #                     # print(str(idx), str(size + idx), substring)
    #                     if self.graph.getEdge(idx, idx + size) is None:
    #                         self.graph.addEdge(idx, idx + size)

    # def make_graph_by_permutations(self, perm_of_str_b):
    #     # add edges by the permutation of str_b on the linear graph of str_a
    #     ans_graph = Graph.Graph()
    #     self.init_graph(ans_graph)  # init graph by str_a
    #     # add edges by perm of str_b
    #     for substring in perm_of_str_b:
    #         size = len(substring)
    #         if size > 1:  # because all substring of len 1 already connected in the graph
    #             matches = re.finditer(substring, self.str_a)
    #             matches_positions = [match.start() for match in matches]
    #             for idx in matches_positions:
    #                 if ans_graph.getEdge(idx, idx + size) is None:
    #                     ans_graph.addEdge(idx, idx + size)
    #     return ans_graph

    # def get_all_bfs_path(self):
    #     # for every permutation of str_b,
    #     #   build a temporary graph by the permutation and check the length with the bfs func
    #     maxSize = len(self.str_a)
    #     ans = []
    #     permutations = self.partitions(self.str_b)
    #     for perm in permutations:
    #         g = self.make_graph_by_permutations(perm)
    #         bfs_g = self.BFS(g.getVertex(0), len(self.str_a))
    #         if len(bfs_g) < maxSize:
    #             maxSize = len(bfs_g)
    #             ans.clear()
    #             ans.append(bfs_g)
    #         elif len(bfs_g) == maxSize:
    #             if bfs_g not in ans:
    #                 ans.append(bfs_g)
    #     return ans

    # def partitions(self, string):
    #     # returns all the partitions of string
    #     for cutpoints in range(1 << (len(string) - 1)):
    #         result = []
    #         result_idx_tmp = []
    #         lastcut = 0
    #         for i in range(len(string) - 1):
    #             if (1 << i) & cutpoints != 0:
    #                 result.append(string[lastcut:(i + 1)])
    #                 result_idx_tmp.append([lastcut, i + 1])
    #                 lastcut = i + 1
    #         result.append(string[lastcut:])
    #
    #         # result_idx_tmp.append([lastcut, len(string)])
    #         # result_idx.append(result_idx_tmp)
    #         yield result
    def is_good(self, str_a, str_b):
        return len(str_a) == len(str_b) and sorted(str_a) == sorted(str_b)

