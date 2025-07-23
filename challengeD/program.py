'''Tariq Fuller
 Challenge D: Football Scores'''
import sys

def main():
    '''Main function which reads in input and output the results '''
    while line := sys.stdin.readline().strip():
        score = int(line)
        football_score(score)


def football_score(target):
    '''Calcualate all ways to score using touchdowns,fields goals, and safetiespyli'''
    plays = [2, 3, 7]
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # Base case

    for play in plays:
        for score in range(play, target + 1):
            for combo in dp[score - play]:
                dp[score].append(combo + [play])

    ways = dp[target]
    count = len(ways)

    if count == 0:
        print(f"There are 0 ways to achieve a score of {target}:")
    elif count == 1:
        print(f"There is 1 way to achieve a score of {target}:")
    else:
        print(f"There are {count} ways to achieve a score of {target}:")
    for combo in sorted(ways):
        print(" ".join(map(str, combo)))


if __name__ == "__main__":
    main()
