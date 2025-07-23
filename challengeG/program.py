'''Tariq Fuller
 Challenge G: Isolated Circuits'''

import sys

def main():
    '''Main function which reads in input and output the results '''
    i = 1
    while line := sys.stdin.readline().strip():
        matrix = []
        n=int(line)
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().strip().split()))
            matrix.append(row)
        print(f"System {i} isolated circuits: {count_components(matrix)}")
        i += 1


def count_components(matrix: list[list[int]]) -> int:
    '''Goes through matrix and count all circuits'''
    n = len(matrix)
    visited = [False] * n
    count = 0

    for i in range(n):
        if visited[i]:
            continue

        stack = [i]
        while stack:
            u = stack.pop()
            if visited[u]:
                continue

            visited[u] = True
            for v in range(n):
                if matrix[u][v] == 1 and not visited[v]:
                    stack.append(v)
        count += 1

    return count

if __name__ == "__main__":
    main()
