'''Tariq Fuller
 Challenge F: Matrix'''
import sys

def main():
    '''Main function which reads in input and output the results '''
    while line := sys.stdin.readline().strip():
        x =list(map(int,line.split()))[0]
        matrix = []
        for _ in range(x):
            row = list(map(int, sys.stdin.readline().strip().split()))
            matrix.append(row)
        min_cost, path = min_weight_path(matrix)
        print(min_cost)
        print(*path)


def min_weight_path(matrix):
    '''Calculates the minimum weight path through a matrix with wrap-around row movement'''
    m, n = len(matrix), len(matrix[0])
    dp = [[float('inf')] * n for _ in range(m)]
    parent = [[-1] * n for _ in range(m)]

    for r in range(m):
        dp[r][0] = matrix[r][0]

    for c in range(1, n):
        for r in range(m):
            prev_rows = sorted([(r - 1) % m, r, (r + 1) % m])
            for prev_r in prev_rows:
                current_cost = dp[prev_r][c - 1] + matrix[r][c]
                if current_cost < dp[r][c]:
                    dp[r][c] = current_cost
                    parent[r][c] = prev_r
                elif current_cost == dp[r][c]:
                    if parent[r][c] == -1 or prev_r < parent[r][c]:
                        parent[r][c] = prev_r

    min_cost = float('inf')
    min_ending_row = -1

    for r in range(m):
        if dp[r][n - 1] < min_cost:
            min_cost = dp[r][n - 1]
            min_ending_row = r
        elif dp[r][n - 1] == min_cost:
            min_ending_row = min(min_ending_row, r)



    path = []
    current_row = min_ending_row
    for c in range(n - 1, -1, -1):
        path.append(current_row)
        if c > 0:
            current_row = parent[current_row][c]

    path.reverse()

    path_1_indexed = [r + 1 for r in path]

    return min_cost, path_1_indexed


if __name__ == "__main__":
    main()
