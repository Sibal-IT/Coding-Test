# 해답 참조: https://merrily-code.tistory.com/207

from sys import stdin
import heapq 

input = stdin.readline

count = 0

n = int(input().strip())
ds = -int(input().strip())
ppl = []

for i in range(n-1):
    temp = int(input().strip())
    # 힙큐를 pop 할 경우, 가장 작은 숫자부터 pop 된다.
    # 이를 가장 큰 숫자부터 불러오기 위한 방법
    heapq.heappush(ppl, -temp)

# 리스트에 값이 있을 경우에만 돌게 설정.
# 만약 혼자 출마했다면 무조건 당선이기 때문
while ppl:
    temp = heapq.heappop(ppl)
    if temp <= ds:
        temp += 1
        ds -= 1
        count += 1
        heapq.heappush(ppl, temp)
    else:
        break


print(count)