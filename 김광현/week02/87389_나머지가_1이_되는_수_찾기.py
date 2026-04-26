# 문제: 나머지가 1이 되는 수 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(1000000):
        if n % (i + 1) == 1:
            return i + 1
