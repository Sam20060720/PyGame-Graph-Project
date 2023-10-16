import os
import sys
import pygame
from mylocals import *
from pygame.locals import *
from Graph import Graph
from Prim import Prim
from Dijkstra import Dijkstra

import time

WIDTH, HEIGHT = 1500, 800

# init pygame and fpsclock
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window
pygame.init()
pygame.display.set_caption('')
surface = pygame.display.set_mode((WIDTH, HEIGHT))
fpsclock = pygame.time.Clock()


algo_menu = {
    'Dijkstra': lambda G: Dijkstra(G),
    'Prim': lambda G, : Prim(G),
}

# get command arguments
try:
    the_seed = DEFAULT_SEED
    if len(sys.argv) >= 2:
        the_seed = int(sys.argv[1])
except:
    the_seed = DEFAULT_SEED

try:
    the_density = DEFAULT_DENSITY
    if len(sys.argv) == 3:
        the_density = int(sys.argv[2])
    if the_density not in range(5, 10+1):
        the_density = DEFAULT_DENSITY
except:
    the_density = DEFAULT_DENSITY

# the_algo = 'Prim'
the_algo = 'Dijkstra'

# generate graph object
G = Graph(randseed=the_seed, v_density=the_density)
edge_list = G.get_all_edges()
vertex_list = G.get_all_vertices()

print(G)
print()
G.print_edges(is_save=True)
G.print_adj_list()
G.print_adj_matrix()

algo = algo_menu[the_algo](G)
# do the algorithm
algo.do_algorithm()
# print the table and path logs
algo.print_table(is_save=True)
log_len = len(algo.get_path_logs())


# draw objects
log_i = -1
nowdraw_i = -1

lastupdate = time.time()
isauto = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and log_i < log_len and nowdraw_i == log_i:
                log_i += 1
            elif event.key == K_f:
                isauto = 1

    if isauto and int(time.time()) - lastupdate >= 0.25 and log_i < log_len:
        lastupdate = time.time()
        log_i += 1

    surface.fill(WHITE)

    nowdraw_i = algo.update_surface(surface, log_i)

    pygame.display.update()

    fpsclock.tick(5)
