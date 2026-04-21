'''
성능 요약
메모리: 9.4 MB
시간: 0.03 ms
'''

def solution(n):
    answer = 0
    arr = list(str(n))
    arr.sort(reverse=True)
    answer = int(''.join(arr))
    return answer