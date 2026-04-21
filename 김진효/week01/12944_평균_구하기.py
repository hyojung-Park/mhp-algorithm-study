'''
성능 요약
메모리: 9.07 MB
시간: 0.01 ms
'''

def solution(arr):
    answer = 0
    s = 0
    for num in arr:
        s += num
    answer = s / len(arr)
    return answer