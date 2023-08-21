from sys import stdin

# 풀이 참조 후 작성완료
# 다음날 다시 작성 후 push
# https://velog.io/@hyungraelee/백준-문제풀이-15729번

def main():
    n = int(input().strip())
    targets = list(map(int, input().split()))
    buttons = [0] * n
    count = 0

    for i, target in enumerate(targets):
        if buttons[i] != target:
            count += 1
            buttons[i:i+3] = map(lambda x: not x, buttons[i:i+3])
    
    print(count)

if __name__ == "__main__":
    main()