 # [성능 요약] 메모리: 745 MB 시간: 1057.17 ms 

def solution(a, b):
    answer = 0
    if a < b:
        answer += sum([i for i in range(a,b+1)])
    else:
        answer += sum([i for i in range(b, a+1)])
    return answer