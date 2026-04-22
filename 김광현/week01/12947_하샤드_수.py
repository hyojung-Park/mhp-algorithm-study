# 문제: 하샤드 수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    sum_state = 0
    for i in str(x):
        sum_state += int(i)
    if x % sum_state == 0:
        return True
    else:
        return False
