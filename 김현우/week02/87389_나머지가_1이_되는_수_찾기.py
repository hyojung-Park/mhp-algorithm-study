# 문제: 나머지가 1이 되는 수 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for x in range(2, int(n**(0.5)+2)):
        if n%x==1: return x
    return n-1