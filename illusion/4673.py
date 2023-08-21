# d(n) 생성용 함수
def solution(number):
    result = number
    add = list(map(int, str(number)))

    for a in add:
        result += a

    return result


# no inputs
def main():
    answer = [True] * 10001

    while_count = 1

    while while_count <= 10000:
        temp = solution(while_count)

        if temp <= 10000:
            answer[temp] = False

        while_count +=1

        # print("cnt:",while_count)
        # print("temp",temp)

    for i in range(1, len(answer)):
        if answer[i]:
            print(i)


if __name__ == "__main__":
    main()


# 9999는 왜 출력되는지 이해가 안되어서 해설 검색
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sskd789&logNo=220845212420
# ex) 1000 > 1000 + 1 + 0 + 0 + 0 > '1001'은 생성자 1000을 가지고 있다
# ex) 9999 > 9999 + 9 + 9 + 9 + 9 > '10035'는 생성자 9999를 가지고 있다

# https://hcr3066.tistory.com/26
# 오늘 배운 것: 브루트 포스 알고리즘
# 완전 탐색으로 푸는 문제로, 말 그대로 "무식하게 힘으로 푸는 알고리즘"이라고 할 수 있다.
# 해가 존재할 것으로 예상되는 모든 영역을 전체탐색하는 것.
# 당연히 자원과 시간을 많이 소모함에도 불구하고 이 알고리즘을 사용하는 이유?
# 예외없이 100%의 확률로 정답을 뽑아내기 때문.