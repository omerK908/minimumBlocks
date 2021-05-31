import re

import Graph

result_idx = []


def all_partitions(string):
    for cutpoints in range(1 << (len(string) - 1)):
        result = []
        result_idx_tmp = []
        lastcut = 0
        for i in range(len(string) - 1):
            if (1 << i) & cutpoints != 0:
                result.append(string[lastcut:(i + 1)])
                result_idx_tmp.append([lastcut, i + 1])
                lastcut = i + 1
        result.append(string[lastcut:])

        result_idx_tmp.append([lastcut, len(string)])
        result_idx.append(result_idx_tmp)
        yield result


class MinimumBlocks(object):

    def __init__(self, str_a, str_b):
        self.graph = Graph.Graph()
        self.str_a = str_a
        self.str_b = str_b
        self.init_graph(self.graph)
        self.make_edges_by_permotations()

        # partitions_of_str_b = self.partitions(str_b)
        # print(len(partitions_of_str_b))
        #
        # if str_a[:1] != str_b[:1]:
        #     partitions_of_str_b = self.filter(lst=partitions_of_str_b, first_letter=str_a[:1])

        # print(filtered_idx)
        # tmp = self.make_edges_by_permotations()

    def init_graph(self, graph):
        for _ in range(len(self.str_a) + 1):
            graph.addVertex()

        for ID in range(0, len(self.str_a)):
            self.graph.addEdge(ID, ID + 1)

    def get_substring(self, edge):
        if edge is None:
            print("get_substring: edge is None")
        return self.str_a[edge.getSrcNode().getId(): edge.getDstNode().getId()]

    def partitions(self, string):
        ans = []
        for partition in all_partitions(string):
            ans.append(partition)
        return ans

    def make_edges_by_permotations(self):
        perm_of_str_b = self.partitions(self.str_b)
        for lst in perm_of_str_b:
            # print(lst)
            for substring in lst:
                size = len(substring)
                if size > 1:  # because all substring of len 1 already connected in the graph
                    matches = re.finditer(substring, self.str_a)
                    matches_positions = [match.start() for match in matches]
                    # print("look here")
                    # print(substring)
                    # print(len(substring))
                    # print(matches_positions)
                    for idx in matches_positions:
                        # print(str(idx), str(size + idx), substring)
                        if self.graph.getEdge(idx, idx + size) is None:
                            self.graph.addEdge(idx, idx + size)

    # def find(self, str, ch):
    #     return [i for i, ltr in enumerate(str) if ltr == ch]

    # def make_graph_by_indexes(self, lst):
    #     graph = Graph.Graph()
    #     for l in lst:
    #         src = l[0]
    #         dst = l[1]
    #         graph.addEdge(src, dst)
    #     return graph

    def filter(self, lst, first_letter):
        ans = []
        for l in lst:
            flag = False
            for str in l:
                if first_letter in str[0:1]:
                    ans.append(l)
                    flag = True
                    break
            if flag:
                pass
        return ans
