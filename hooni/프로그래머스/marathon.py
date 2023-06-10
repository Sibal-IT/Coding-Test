## 프로그래머스 달리기 경주

##문제 설명
##얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

##선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

#1번째 코드
def solution(players, callings):
    answer = []
    temp = ''
    for i in range(len(callings)) :
        for j in range(len(players)):
            if players[j] == callings[i] :
                temp = players[j-1] 
                players[j-1] = players[j]
                players[j] = temp
                break
                
    return players

    #2번째 코드 - dictionary
    def solution(players, callings):
    answer = []
    i_temp = 0
    p_temp = ''
    p_dict = dict()
    i_dict = dict()
    for i in range(len(players)):
        i_dict[players[i]] = i
        p_dict[i] = players[i]
    
    for i in range(len(callings)):
        now_i   = int(i_dict.get(callings[i]))
        front_i = now_i - 1 
        
        now_p   = callings[i]
        front_p = p_dict[front_i]
        
        p_dict[now_i], p_dict[front_i] = front_p, now_p
        i_dict[now_p], i_dict[front_p] = front_i, now_i
        
    for i in p_dict:
        answer.append(p_dict.get(i))
                
    return answer