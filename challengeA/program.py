'''Tariq Fuller
 Challenge A: Challenge A: Views of Sunrise'''
import sys

def main():
    '''Main function which reads in input and output the results '''
    while line := sys.stdin.readline().strip():
        print(count_buildings(list(map(int,line.split()))))

def count_buildings(buildings):
    '''Goes through the list backwards and check
    if the building is tall enough to look past the biggest
    buiding in front of it'''
    max_height = float('-inf')
    count = 0

    for i in range(len(buildings) - 1, -1, -1):
        height = buildings[i]
        if height > max_height:
            count += 1
            max_height = height
    return count

if __name__ == "__main__":
    main()
