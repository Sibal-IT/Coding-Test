from sys import stdin

def main():
    input = stdin.readline
    n = int(input().strip())
    lights = list(map(int, input().split()))
    print(solution(n, lights))

def solution(n, lights):
    buttons = [0] * n
    answer = 0

    for i, light in enumerate(lights):
        if buttons[i] != light:
            buttons[i:i+3] = map(lambda x: not x, buttons[i:i+3])
            answer += 1

    return answer

if __name__ == "__main__":
    main()