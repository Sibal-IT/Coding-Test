## 등수 매기기

import sys

input = sys.stdin.readline

# def main():
#     n = int(input())
#     arr = list(int(input()) for _ in range(n))
#     arr.sort(reverse=True)
#     result = list(True for _ in range(n))
#     answer1 = list()
#     answer2 = list()
#     for i in arr:
#         if result[i - 1]:
#             result[i - 1] = False
#         else:
#             answer1.append(i)

#     for i in range(len(result)):
#         if result[i]:
#             answer2.append(i + 1)

#     answer1.sort()
#     answer2.sort()
#     tot = 0
#     while True:
#         if not answer1 or not answer2:
#             break
#         tot += abs(answer1.pop() - answer2.pop())
#     print(tot)
def main():
    n = int(input())
    arr = list(int(input()) for _ in range(n))
    arr.sort()

    answer = 0
    for i in range(1, n + 1):
        answer += abs(i - arr[i-1])
    
    print(answer)

if __name__ == "__main__":
    main()