import itertools

n = input()
numbers = list(i for i in n)

# permutationed = sorted([i for i in itertools.permutations(numbers, len(numbers)) if i[0] != 0], reverse=True)
permutationed = sorted(list(map(''.join, itertools.permutations(numbers))), reverse=True)
# print(permutationed)

for p in permutationed:
    if int(p) % 30 == 0:
        print(int(p))
        break
    else:
        continue

# 시간초과?
# 남욱스: 그리디를 완탐으로 풀면 당연히 시간초과되지
# 그래서 해답을 봤읍니다
