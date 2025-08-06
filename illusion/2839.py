from sys import stdin

def sugar_bongdari():

    # 봉다리 옵션: 3 or 5
    n = int(stdin.readline())
    
    kg5 = n // 5
    kg3 = 0

    while True:
        # print('kg5:', kg5)
        
        if kg5 == 1:
            temp = n - 5
        elif kg5 > 1:
            temp = n - (kg5 * 5) # 처음에 % 연산자를 사용했는데, 반례 22 사용하여 수정
            # print('temp1:', temp)
        else:
            if n % 3 == 0:
                return n // 3
            return -1
        
        if temp % 3 == 0:
            # print('temp2:', temp)
            kg3 = temp // 3
            # print('kg3:', kg3)
            break
        else:
            kg5 -= 1
                  
    return kg5 + kg3

print(sugar_bongdari())