from Text import Text
from mylocals import *
import sys

INF = sys.maxsize


class Dijkstra():
    def __init__(self, graph):
        self.graph = graph
        self.dist = {}
        self.prev = {}
        self.log = []
        self.Q = []
        self.init_table()

        self.start_v = None
        self.vertex_header = None
        self.log_len = 0
        self.log_texts = []

    def init_table(self, start_v='A'):
        for vi in self.graph.vertices:
            self.dist[vi] = INF
            self.prev[vi] = None
            self.Q.append(vi)
        self.dist[self.graph.getVertex(start_v)] = 0
        self.start_v = self.graph.getVertex(start_v)

    def do_algorithm(self):
        while len(self.Q) != 0:
            u = self.get_min_Vertex(self.start_v)
            if u is None:
                break
            self.Q.remove(u)
            neig = self.graph.get_all_neighbors(u)  # 臨邊的點
            if neig is not None:
                for v in neig.keys():
                    if v in self.Q:
                        alt = self.dist[u] + \
                            self.graph.get_edge(u, v).get_weight()
                        if alt < self.dist[v]:
                            self.dist[v] = alt
                            self.prev[v] = u

            tempdist = self.dist.copy()
            tempdist['u'] = u.get_name()
            self.log.append(tempdist.copy())
        self.init_surface()
        return self.dist, self.prev

    def get_dist_log(self):
        log_opt = []
        for row in self.log:
            row_opt = ["-"] * len(self.graph.vertices)
            for i in row.keys():
                if i != 'u':
                    row_opt[ord(i.get_name()) - ord('A')
                            ] = row[i] if row[i] != INF else "-"
            log_opt.append([row['u']]+row_opt)
        # print(len(log_opt), len(self.prev))
        return log_opt

    def print_table(self, is_save=False):
        if is_save:
            with open("atable.txt", "w+") as fp:
                for i in self.dist.keys():
                    fp.write(f"{i} : {self.dist[i]}\r\n")

        for i in self.dist.keys():
            print(f"{i} : {self.dist[i]}")

    def get_min_Vertex(self, v):  # 在dist中取得距離v最短的頂點
        min = INF
        min_v = None
        for vi in self.Q:
            if self.dist[vi] < min:
                min = self.dist[vi]
                min_v = vi

        return min_v

    def get_vertex_names(self):
        names = ""
        for v in self.graph.vertices:
            names += f'{v.get_name():>3}'
        return names

    def get_path_logs(self):
        return self.dist_log

    def init_surface(self):
        self.vertex_header = Text(
            (950, 20), text=self.get_vertex_names(), size=18)
        # # generate log texts
        self.dist_log = self.get_dist_log()
        self.log_len = len(self.dist_log)
        self.log_texts = []
        dists = []
        log_y = 40
        for row in self.dist_log:
            dists.clear()
            for dist in row:
                dists.append(f'{dist:>3}')
            log_line = ''.join(dists)
            self.log_texts.append(Text((930, log_y), text=log_line, size=18))
            log_y += 20
        self.log_texts.append(
            Text((930, log_y), text='  Done', size=18, color=RED))

    def update_surface(self, surface, log_i):
        self.vertex_header.draw(surface)
        if log_i >= 0:
            for log_t in self.log_texts[:log_i+1]:
                log_t.draw(surface)

        for i, edge in enumerate(self.graph.get_all_edges()):
            edge.draw(surface)
        for i, vertex in enumerate(self.graph.get_all_vertices()):
            # update the caption color and distance of the vertex
            # print(i, vertex.get_name())
            if 0 <= log_i < self.log_len:
                if vertex.get_name() == self.dist_log[log_i][0]:
                    vertex.set_caption_color(RED)
                dist = self.dist_log[log_i][i+1]
                if isinstance(dist, int):
                    vertex.set_dist_text(surface, dist)
            vertex.draw(surface)
        return log_i
