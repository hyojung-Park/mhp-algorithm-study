# 문제: 음양 더하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    a = len(absolutes)
    answer = 0
    for i in range(a):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer