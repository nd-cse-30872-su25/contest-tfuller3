'''Tariq Fuller
Challenge E: Tree Paths'''
import sys
from typing import List, Optional
from dataclasses import dataclass


def main():
    '''Main function which reads in input and output the results '''
    while line := sys.stdin.readline().strip():
        target = int(line.strip())
        if target == 0:
            break
        values = list(map(int, sys.stdin.readline().strip().split()))
        root = build_tree(values)
        results = []
        find_paths(root, target, [], results)
        results.sort()
        for path in results:
            print(f"{target}: {', '.join(map(str, path))}")

@dataclass
class Node:
    ''' Node Structure '''
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

def build_tree(values: List[int]) -> Optional[Node]:
    '''Bulding the Tree'''
    if not values or values[0] == 0:
        return None
    nodes = [Node(v) if v != 0 else None for v in values]
    for i, node in enumerate(nodes):
        if node:
            li, ri = 2 * i + 1, 2 * i + 2
            if li < len(nodes):
                node.left = nodes[li]
            if ri < len(nodes):
                node.right = nodes[ri]
    return nodes[0]

def find_paths(node: Optional[Node], target: int, path: List[int], results: List[List[int]]):
    '''Searching through the path and finding path with target'''
    if not node:
        return
    path.append(node.value)
    target -= node.value
    if not node.left and not node.right and target == 0:
        results.append(path[:])
    find_paths(node.left, target, path, results)
    find_paths(node.right, target, path, results)
    path.pop()

if __name__ == "__main__":
    main()
