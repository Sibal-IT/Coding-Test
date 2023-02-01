from sys import stdin

def solution(n, m, price):
    answer = 0
    left = 0

    package_price = sorted(price, key=lambda x: x[0])
    single_price = sorted(price, key=lambda x: x[1])

    # print(package_price)
    # print(single_price)

    # if문에서 뭘 판별해야 하는가?
    # 6개당 비용이 세트가 저렴한지, 낱개가 저렴한지
    if package_price[0][0] < single_price[0][1] * 6:
        answer += package_price[0][0] * (n // 6)
        left = n % 6
    else:
        answer += single_price[0][1] * n

    # 자 이제 남은 수량을 어떻게 해결할 것인지 고민해보자.
    # 만약 목표 수량을 초과하더라도 6개 세트를 하나 더 추가하는 것이 저렴하다면?
    if left > 0:
        if package_price[0][0] < single_price[0][1] * left:
            answer += package_price[0][0]
        else:
            answer += single_price[0][1] * left

    return answer

def main():
    input = stdin.readline
    N, M = map(int, input().split())
    price = [list(map(int, input().split())) for _ in range(M)]
    
    print(solution(N, M, price))

if __name__ == "__main__":
    main()