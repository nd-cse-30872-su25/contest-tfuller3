'''Tariq Fuller
 Challenge A: Challenge A: Views of Sunrise'''
import sys

def main():
    '''Main function which reads in input and output the results '''
    while line := sys.stdin.readline().strip():
        s,t=line.split()
        if is_isomorphic(s,t):
            print("Isomorphic")
        else:
            print("Not Isomorphic")

def is_isomorphic(s:str,t:str) -> bool:
    '''Determine if the two words are isomorphic or not'''
    if len(s) != len(t):
        return False

    map_s_t = [-1] * 128
    map_t_s = [-1] * 128

    for i in range(len(s)):
        c1 = ord(s[i])
        c2 = ord(t[i])

        if map_s_t[c1] == -1 and map_t_s[c2] == -1:
            map_s_t[c1] = c2
            map_t_s[c2] = c1
        elif map_s_t[c1] != c2 or map_t_s[c2] != c1:
            return False

    return True

if __name__ == "__main__":
    main()
