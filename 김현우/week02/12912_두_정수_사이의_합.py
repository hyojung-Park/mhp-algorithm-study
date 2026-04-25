# 문제: 두 정수 사이의 합
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    if a==b: return a
    return (a+b)*(abs(a-b)+1)/2
