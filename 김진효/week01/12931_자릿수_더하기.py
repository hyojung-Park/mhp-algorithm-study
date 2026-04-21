'''
성능 요약
메모리: 9.06 MB
'''

def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10 
        n //= 10


    return answer