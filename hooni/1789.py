import sys

input = sys.stdin.readline

def main():
    s = int(input())
    sum_ = 0
    if s == 1:
        print(1)
        return
    elif s == 2:
        print(1)
        return
    elif s == 3:
        print(2)
        return
    for i in range(1, s):
        sum_ += i
        if sum_ > s:
            print (i - 1)
            return
    
if __name__ == "__main__":
    main()