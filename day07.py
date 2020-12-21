import networkx as nx

from collections import defaultdict
from typing import Dict, List, Tuple

from networkx.algorithms import topological_sort
from networkx.algorithms.traversal.depth_first_search import dfs_successors, dfs_tree
from treelib import Node, Tree


def parse_contents(contents: str) -> List[Tuple[int, str]]:
  if contents == 'no other bags.':
    return []

  ret = []
  for bag in contents[:-1].split(', '):
    data = bag.split(' ', 1)
    data[0] = int(data[0])
    data[1] = ' '.join(data[1].split(' ')[:-1])
    ret.append(tuple(data))
  return ret

with open('input/day07.txt') as f:
  lines = f.readlines()

# Graph mapping from outer to inner
G = nx.DiGraph()

for line in lines:
  outside_color, contents = line.strip().split(' bags contain ')
  G.add_node(outside_color)

  for n, inside_color in parse_contents(contents):
    G.add_edge(outside_color, inside_color, weight=n)

count = 0
for node in G.nodes():
  if node != 'shiny gold' and 'shiny gold' in dfs_tree(G, node):
    count += 1

print('Part 1:', count)


store = dict()
def num_contained(G, bag) -> int:
  if bag not in store:
    store[bag] = sum([G.edges[bag, child]['weight'] * (num_contained(G, child) + 1) for child in G[bag]])
  return store[bag]

print('Part 2:', num_contained(G, 'shiny gold'))