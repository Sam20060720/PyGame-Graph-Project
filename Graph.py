import sys
import random
from Vertex import Vertex
from Edge import Edge
from mylocals import *
INF = sys.maxsize


class Graph():
    def __init__(self, randseed=1, v_density=10):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.randseed = randseed
        self.v_density = v_density
        self.adj_list = {}
        self.adj_matrix = []
        self.vertices = self.add_all_vertices()
        self.edges = self.add_all_edges()
        self.create_adj_list()
        self.create_adj_matrix()
        # self.print_adj_list()

    def __repr__(self):
        return f"Graph<{len(self.vertices)} vertices, {len(self.edges)} edges>"

    def add_all_vertices(self):
        vertuces = []
        now_alphabet = 0
        for i in range(0, 500, 100):
            for j in range(0, 500, 100):
                vert_dense = random.randint(0, 10)
                if vert_dense <= self.v_density:
                    # vertuces.append(
                    #     Vertex((i+50, j+50), chr(i // 100 * 5 + j // 100 + 65)))
                    vertuces.append(
                        Vertex((i+50, j+50), chr(65+now_alphabet)))
                    now_alphabet += 1
        return vertuces

    def get_all_vertices(self):
        return self.vertices

    def add_all_edges(self):
        edges = []
        tempe = []
        # 判斷是否相鄰
        for i in self.vertices:
            for j in self.vertices:
                if i != j:
                    if (i.get_position()[0] == j.get_position()[0] and abs(i.get_position()[1] - j.get_position()[1]) == 100) or (i.get_position()[1] == j.get_position()[1] and abs(i.get_position()[0] - j.get_position()[0]) == 100):
                        # print(i.get_position(), j.get_position())
                        if (i.get_name(), j.get_name()) not in tempe and (j.get_name(), i.get_name()) not in tempe:
                            weight = random.randint(
                                WEIGHT_RANGE[0], WEIGHT_RANGE[1])
                            edges.append(Edge(i, j,
                                              i.get_position(), j.get_position(), weight=weight))
                            tempe.append((i.get_name(), j.get_name()))

        return edges

    def get_all_edges(self):
        return self.edges

    def get_edge(self, u, v, isinv=True):  # isinv : 是否能反過來取得邊
        u = self.getVertex(u)
        v = self.getVertex(v)
        # print(u, v)
        if u is None or v is None:
            return None
        if u == v:
            return u
        for edge in self.edges:
            if edge.vertex1 == u and edge.vertex2 == v:
                return edge
            if isinv and edge.vertex1 == v and edge.vertex2 == u:
                return edge
        return None

    def print_edges(self, is_save=False):
        # print('Edge List:')
        for edge in self.edges:
            print(edge)
        if is_save:
            with open("save.txt", "w+") as fp:
                for i in self.edges:
                    fp.write(i.get_raw() + '\r\n')

    def create_adj_list(self):
        for iedge in self.edges:
            if iedge.vertex1 not in self.adj_list.keys():
                self.adj_list[iedge.vertex1] = {}
            self.adj_list[iedge.vertex1][iedge.vertex2] = iedge.get_weight()

        for iedge in self.edges:
            if iedge.vertex2 not in self.adj_list.keys():
                self.adj_list[iedge.vertex2] = {}
            self.adj_list[iedge.vertex2][iedge.vertex1] = iedge.get_weight()

    def print_adj_list(self):
        for i in self.adj_list.keys():
            print(f"{i} : {self.adj_list[i]}")

    def create_adj_matrix(self):
        self.adj_matrix = []
        for i in range(0, len(self.alphabet)):
            tempmatrix = []
            for j in range(0, len(self.alphabet)):
                appendx = self.get_edge(
                    list(self.alphabet)[j], list(self.alphabet)[i])
                tempmatrix.append(
                    appendx.get_weight() if appendx is not None else sys.maxsize)
            self.adj_matrix.append(tempmatrix)

    def get_adj_matrix(self):
        return self.adj_matrix

    def print_adj_matrix(self):
        print("  ", end="")
        for i in range(0, len(self.alphabet)):
            print(self.alphabet[i], end=" ")
        print()
        for i in range(0, len(self.alphabet)):
            print(self.alphabet[i], end=" ")
            for j in range(0, len(self.alphabet)):
                print(self.adj_matrix[i][j] if self.adj_matrix[i]
                      [j] != sys.maxsize else "-", end=" ")
            print()
        print()

    def getVertex(self, name):
        if type(name) == Vertex:
            return name
        for i in self.vertices:
            if i.get_name() == name:
                return i
        return None

    def get_all_neighbors(self, u):
        if type(u) == str:
            u = self.getVertex(u)
        if u is None:
            return None

        return self.adj_list.get(u)
