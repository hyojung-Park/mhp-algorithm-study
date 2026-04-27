 # [성능 요약] 메모리: 9.04 MB 시간: 0.01 ms 

def solution(s):
    answer = True
    
    s = s.upper()
    
    p = s.count('P')
    s = s.count('Y') 

    if p != s:
        answer = False
    
    return answer