# 3-1
from sys import stdin

def coins():

    input = int(stdin.readline())
    result = 0

    coins_list = [500, 100, 50, 10]

    for coin in coins_list:
        if input / coin > 0:
            print('input//coin:', input//coin)
            result += input//coin
            input = input % coin
            print('남은 돈:', input)
    
    return result


# 큰 수의 법칙 해설 참고
def big_num():

    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    result = 0

    print(data)

    big1 = data[-1]
    big2 = data[-2]

    while True:
        for i in range(k):
            if m == 0:
                break
                
            result += big1
            m -= 1
        
        if m == 0:
            break

        result += big2
        m-=1

    return result



def card_game():
    result = 0

    n, m = map(int, input().split())

    min_card_list = []

    for _ in range(n):
        temp_card_list = list(map(int, input().split()))
        min_card_list.append(min(temp_card_list))

    return max(min_card_list)



def while_one():

    n, k = map(int, input().split())
    
    result = 0

    while n > 1:
        
        if n % k == 0:
            n = n // k
            print(n)
            result += 1
        else:
            n = n - 1
            print(n)
            result += 1
        
    return result




# print(coins())
# print(big_num())
# print(card_game())
print(while_one())