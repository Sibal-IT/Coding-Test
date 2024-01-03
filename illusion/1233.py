from itertools import product

s1, s2, s3 = map(int, input().split())

s1_list = [i+1 for i in range(s1)]
s2_list = [i+1 for i in range(s2)]
s3_list = [i+1 for i in range(s3)]

temp = list(product(s1_list, s2_list, s3_list))

for i, t in enumerate(temp):
    temp[i] = str(sum(t))

count = {}

for t in temp:
    try: count[t] += 1
    except: count[t] = 1

print(sorted(count.items(), key=lambda x: x[1], reverse=True)[0][0])


# 두 개 이상의 리스트에서 모든 조합 구하기
# https://lar542.github.io/Python/2019-07-11-python2/

# 딕셔너리에서 중복값 개수 체크하기
# https://infinitt.tistory.com/78

# 딕셔너리에서 중복값 개수 가장 많은 값 호출하기
# max(same, key=same.get)
# 이건 안씀