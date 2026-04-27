 # [성능 요약] 메모리: 9.16 MB 시간: 69.86 ms 

def solution(n):
    answer = 0
    for x in range(1,n):
        if n % x == 1:
            answer = x
            break
    return answer