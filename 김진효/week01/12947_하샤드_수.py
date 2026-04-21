'''
성능 요약
메모리: 9.25 MB
시간: 0.03 ms
'''

def solution(x):
    answer = True
    
    s = 0
    for num in str(x):
        s += int(num)
        
    if x % s != 0:
        answer = False 
        
    return answer