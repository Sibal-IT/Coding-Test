from sys import stdin

input = stdin.readline

# def solution(n, ds, ppl):
#     if n == 1:
#         return 0
#     elif n > 1 and len(ppl) == 0:
#         return 1
#     else:
#         temp_ds = ds
#         temp_ppl = ppl

#         for tp in temp_ppl:
#             if tp > temp_ds:
#                 tp -= 1
#                 temp_ds + 1


# n = int(input())
# ds = int(input())
# ppl = []

# for _ in range(n-1):
#     temp = int(input())
#     if temp > ds:
#         ppl.append(temp)
#     else:
#         pass


# print(solution(n, ds, ppl))
# 예 뭐 안해본건 아닌데, 도저히 모르겠더라고요.
# 찾아보니 우선순위 큐 heapq를 import 해서 쓰라네요.