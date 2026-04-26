# 문제: 문자열 내 p와 y의 개수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    p_num = 0
    y_num = 0
    s = s.lower()

    for i in s:
        if i == 'p':
            p_num += 1
        elif i == 'y':
            y_num += 1
    if p_num == y_num:
        return answer
    else:
        answer = False
        return answer