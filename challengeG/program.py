import sys



def main():
    i = 1
    while line := sys.stdin.readline().strip():
        matrix = []
        n=int(line)
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().strip().split()))
            matrix.append(row)
        result = count_components(matrix)
        print(f"System {i} isolated circuits: {result}")
        i += 1


def count_components(matrix):
    n = len(matrix)
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    for v in range(n):
                        if matrix[u][v] == 1 and not visited[v]:
                            stack.append(v)
            count += 1

    return count

if __name__ == "__main__":
    main()