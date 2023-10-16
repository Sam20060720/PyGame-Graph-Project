import sys
from mylocals import *
from Text import Text

INF = sys.maxsize


class Prim():
    def __init__(self, graph):
        self.graph = graph
        self.mst_vertices = set()  # 走訪過的點
        self.mst_edges = set()  # 走訪過的邊
        self.graphVertex = set()  # Graph.Vertices 的集合
        self.log = []
        self.log_edge = []
        self.log_len = 0
        self.log_texts = []
        self.start_v = None

        self.init_table()

    def init_table(self, start_v='A'):
        self.start_v = self.graph.getVertex(start_v)
        self.mst_vertices.add(self.start_v)
        self.mst_edges = set()
        self.graphVertex = set(self.graph.vertices)

    def get_vertex_names(self):
        names = ""
        for v in self.graph.vertices:
            names += f'{v.get_name():>3}'
        return names

    def do_algorithm(self,):
        while self.mst_vertices != self.graphVertex:
            edge = self.get_min_neighbors()  # 取得最小編
            if edge is None:
                break

            self.mst_edges.add(edge)
            self.mst_vertices.add(edge.get_destination())
            self.mst_vertices.add(edge.get_source())

            temp = self.mst_vertices.copy()
            temp.add(edge.get_source())
            self.log.append(temp)
            self.log_texts.append(
                f'{edge.get_source().get_name()} -> {edge.get_destination().get_name()} : {edge.get_weight()}')
            self.log_edge.append(edge)

        self.log_len = len(self.log_edge)
        if self.mst_vertices != self.graphVertex:
            self.log_texts.append('Done : No MST')
        else:
            self.log_texts.append('Done : MST')
        self.init_surface()

    def get_min_neighbors(self):
        u = self.mst_vertices
        v = self.graphVertex - self.mst_vertices  # 未走訪
        min_ = INF
        min_edge = None
        for i in u:
            for j in v:
                if self.graph.get_edge(i, j, isinv=True) is not None:
                    if self.graph.get_edge(i, j, isinv=True).get_weight() < min_:
                        min_ = self.graph.get_edge(
                            i, j, isinv=True).get_weight()
                        min_edge = self.graph.get_edge(i, j, isinv=True)
        return min_edge

    def get_path_logs(self):
        return self.log

    def create_path_log_texts(self):
        pass

    def print_path_logs(self):
        pass

    def print_table(self, is_save=False):
        pass

    def init_surface(self):
        # cover Text str to Text object
        self.log_texts_org = self.log_texts.copy()
        for i, log_t in enumerate(self.log_texts):
            self.log_texts[i] = Text((930, 20 + 20 * i), log_t, 20, BLACK)

    def update_surface(self, surface, log_i):
        if log_i >= 0:
            for log_t in self.log_texts[:log_i+1]:
                log_t.draw(surface)

        for i, edge in enumerate(self.graph.get_all_edges()):
            edge.draw(surface)

        for i, vertex in enumerate(self.graph.get_all_vertices()):
            if 0 <= log_i < self.log_len:
                if vertex in self.log[log_i]:
                    vertex.set_caption_color(RED)
                else:
                    vertex.set_caption_color(BLACK)
                self.log_edge[log_i].set_color(RED)

            vertex.draw(surface)

        if log_i == self.log_len - 1:
            for i in (set(self.graph.get_all_edges()) - set(self.log_edge)):
                i.hide()
            self.log_texts[len(self.log_texts)-1].draw(surface)

        return log_i
