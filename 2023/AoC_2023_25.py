from math import prod
import networkx as nx

g = nx.Graph()
for line in open("AoC_2023_25.txt").read().split("\n"):
  component, connections = line.split(": ")
  for c in connections.split():
    g.add_edge(component, c)
g.remove_edges_from(nx.minimum_edge_cut(g))

print('Part 1: %s; part 2: %s' % (prod(len(c) for c in nx.connected_components(g)), 'free! Finished with Advent of Code 2023!!!'))
