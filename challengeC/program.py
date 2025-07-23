'''Tariq Fuller
 Challenge A: Challenge A: Views of Sunrise'''
import sys

def main():
    '''Main function which reads in input and output the results '''
    while line := sys.stdin.readline().strip():
        find_expression(int(line))

def find_expression(target):
    '''Starts the recursive expression and give operation list'''
    ops = ['+', '-', '*']
    pattern = "(((9 {} 8) {} 7) {} 6) {} (5 {} (4 {} (3 {} (2 {} 1))))"

    def recurse(depth, current_ops):
        '''Recursive function to go to next operation '''
        if depth == 8:
            expr = pattern.format(*current_ops)
            try:
                if eval(expr) == target:
                    print(f"{expr} = {target}")
                    return True
            except ValueError:
                return False
            return False
        for op in ops:
            if recurse(depth + 1, current_ops + [op]):
                return True
        return False

    if not recurse(0, []):
        print("No expression found.")

if __name__ == "__main__":
    main()
