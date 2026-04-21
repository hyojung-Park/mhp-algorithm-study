'''
성능 요약
메모리 9.3 MB
시간 0.27 ms
'''

def solution(n):
    
    answer = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    
    return answer