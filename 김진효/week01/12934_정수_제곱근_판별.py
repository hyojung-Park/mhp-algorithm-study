'''
성능 요약
메모리: 9.15 MB
시간: 0.01 ms
'''

import math 

def solution(n):
    answer = -1
    # x = math.sqrt(n)
    x = int(math.sqrt(n))
    
    if x ** 2 == n:
        answer = (x + 1)**2
        
    return answer

