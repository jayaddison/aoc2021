from collections import defaultdict
from itertools import permutations
import sys

height, width = 0, 0
nodes_by_frequency = defaultdict(list)
antinodes = set()

def generate_antinodes(a, b):
    (a_y, a_x), (b_y, b_x) = a, b
    (delta_y, delta_x) = (b_y - a_y), (b_x - a_x)
    antinode_alpha = (a_y - delta_y, a_x - delta_x)
    antinode_omega = (b_y + delta_y, b_x + delta_x)
    for antinode in antinode_alpha, antinode_omega:
        antinode_y, antinode_x = antinode
        if 0 <= antinode_y <= height and 0 <= antinode_x <= width:
            yield antinode

for idy, line in enumerate(sys.stdin.read().splitlines()):
    height = max(height, idy)
    for idx, char in enumerate(line):
        width = max(width, idx)
        if char == ".":
            continue
        nodes_by_frequency[char].append((idy, idx))

for frequency, nodes in nodes_by_frequency.items():
    for node_a, node_b in permutations(nodes, r=2):
        for antinode in generate_antinodes(node_a, node_b):
            antinodes.add(antinode)
print(len(antinodes))
