import sys
from collections import deque


def main():
    n, m = map(int, input().split())
    arr = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
    q = deque(arr)
    cnt = 1
    while True:
        cur = q.popleft()
        if any(cur[1] < x[1] for x in q):
            q.append(cur)
            # cnt += 1
        else:
            if cur[0] == m:
                print (cnt)
                break
            else:
                cnt += 1
        

if __name__ == "__main__":
    main()
