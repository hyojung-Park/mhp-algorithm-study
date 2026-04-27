 # [성능 요약] 메모리: 8.98 MB 시간: 0.01 ms 

def solution(numbers):
    answer = 0
    s = set(numbers)
    for i in range(10):
        if i not in s:
            answer += i
    return answer