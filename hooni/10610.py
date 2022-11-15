import sys
from itertools import permutations

# input = sys.stdin.readline

def main():
    n = input()
    if "0" not in n:
        print(-1)
    else:
        n_sum = 0
        for i in n[:]:
            n_sum += int(i)
        if n_sum % 3 == 0:
            print("".join(sorted(n, reverse=True)))
        else:
            print(-1)

if __name__ == "__main__":
    main()