from sys import stdin

def solution(n, sample):
    answer = 0
    
    for i in range(n):
        temp = 0
        for j in range(i+1, n):
            if sample[i] < sample[j]:
                break
            elif sample[i] > sample[j]:
                temp += 1
        
        answer = max(answer, temp)
        if answer > n - i:
            break

    return answer

def main():
    input = stdin.readline
    n = int(input().strip())
    hanzo = list(map(int, input().split()))

    print(solution(n, hanzo))

if __name__ == "__main__":
    main()