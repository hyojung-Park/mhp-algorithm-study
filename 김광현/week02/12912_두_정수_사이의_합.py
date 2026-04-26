# 문제: 두 정수 사이의 합
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    small_num = 10000000
    large_num = -10000000
    if a < b:
        small_num = a
        large_num = b
    elif a == b:
        return a
    else:
        small_num = b
        large_num = a
    for i in range(small_num, large_num + 1, 1):
        answer += i
    return answer