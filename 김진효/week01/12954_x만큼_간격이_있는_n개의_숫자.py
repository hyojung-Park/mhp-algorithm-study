'''
성능 요약
메모리: 9.26 MB
시간: 0.09 ms
'''

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer