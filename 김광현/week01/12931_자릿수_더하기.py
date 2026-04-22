# 문제: 자릿수 더하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    state = str(n)
    answer = 0
    for i in state:
        answer = answer + int(i)
    return answer