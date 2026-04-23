# 문제: 정수 제곱근 판별
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    for i in range(8000000):
        if i * i == n:
            return ((i + 1) * (i + 1))
        if i * i > n:
            return -1