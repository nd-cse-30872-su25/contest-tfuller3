'''Tariq Fuller
Challenge H: Niblings '''
import sys
from collections import defaultdict

def parse_family_data(lines, i):
    '''Getting family and setting it up'''
    parent_to_children = {}
    child_to_parents = {}
    spouses = {}
    people = set()

    num_families = int(lines[i])
    i += 1

    for _ in range(num_families):
        parts = lines[i].replace(':', '').split()
        i += 1
        p1, p2, *children = parts
        spouses[p1] = p2
        spouses[p2] = p1

        for parent in (p1, p2):
            if parent not in parent_to_children:
                parent_to_children[parent] = []

        for child in children:
            parent_to_children[p1].append(child)
            parent_to_children[p2].append(child)

            if child not in child_to_parents:
                child_to_parents[child] = []
            child_to_parents[child].extend([p1, p2])

        people.update([p1, p2] + children)

    return parent_to_children, child_to_parents, spouses, i

def build_siblings_optimized(child_to_parents):
    '''Build Siblings'''
    siblings = defaultdict(set)
    # Group children by parent or parent pair
    parent_pair_to_children = defaultdict(set)

    for child, parents in child_to_parents.items():
        key = tuple(sorted(parents))  # Ensure consistent key
        parent_pair_to_children[key].add(child)

    for children in parent_pair_to_children.values():
        for child in children:
            siblings[child].update(children - {child})  # All others are siblings

    return siblings

def process_givers(lines, i, parent_to_children, siblings, spouses):
    '''Checking to see if you get gifts'''
    num_givers = int(lines[i])
    i += 1
    for _ in range(num_givers):
        giver = lines[i].strip()
        i += 1
        targets = set()
        sibs = siblings.get(giver, set()) | siblings.get(spouses.get(giver, ''), set())
        for sib in sibs:
            targets.update(parent_to_children.get(sib, []))
        if targets:
            print(f"{giver} needs to buy gifts for: {', '.join(sorted(targets))}")
        else:
            print(f"{giver} does not need to buy gifts")
    return i

def main():
    '''Main function which reads in input and output the results '''
    lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip() == '0':
            break
        ptc, ctp, spouses, i = parse_family_data(lines, i)
        siblings = build_siblings_optimized(ctp)
        i = process_givers(lines, i, ptc, siblings, spouses)

if __name__ == "__main__":
    main()
