# 문제: 문자열 내 p와 y의 개수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = 1

    for x in s:
        if x == 'P' or x == 'p':
            answer += 1
        elif x == 'Y' or x == 'y':
            answer -= 1

    return (answer == True)
