'''
성능 요약
메모리: 9.18 MB
시간: 0.02 ms
'''

def solution(n):
    answer = []
    while n > 0:
        answer.append(n%10)
        n //= 10
    return answer

'''
성능 요약
메모리: 9.36 MB
시간: 0.02 ms
'''
def solution_2(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer

