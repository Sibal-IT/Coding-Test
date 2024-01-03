from sys import stdin

input = stdin.readline

def main():
    answer = 0
    n, k = map(int, input().split())
    coins = sorted([int(input().strip()) for _ in range(n)], reverse=True)


    for c in coins:
        if k // c >= 1:
            answer += (k // c)
            k %= c
    
    print(answer)

if __name__ == "__main__":
    main()