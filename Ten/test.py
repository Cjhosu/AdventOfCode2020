"""
from typing import Dict, List
adapters = [0,1,4,5,6,7,10,11,12,15,16,19,22]
graph = {}

for adapter in adapters:
    potential_neighbors = [adapter + x for x in (1, 2, 3)]
    graph[adapter] = [n for n in potential_neighbors if n in adapters]
    print(graph)

paths = {0: 1}

for adapter, neighbors in graph.items():
    for neighbor in neighbors:
        if neighbor in paths:
            paths[neighbor] += paths[adapter]
        else:
            paths[neighbor] = paths[adapter]
    print(paths)
    """
from collections import defaultdict

paths = defaultdict(int)
#paths = {}
adapters = [0,1,2,3,4,5,8]
paths[0] = 1
print(paths)

for adapter in sorted(adapters):
    for diff in range(1, 4):
        next_adapter = adapter + diff
        if next_adapter in adapters:
            paths[next_adapter] += paths[adapter]
            print(paths)
