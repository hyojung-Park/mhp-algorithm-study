 # [성능 요약] 메모리: 9.25 MB 시간: 0.00 ms 

def solution(s):
    answer = ''
    l = len(s)
    center = l // 2

    if l % 2 == 0:
        answer = s[center-1:center+1]
    else:
        answer = s[center]
        
    return answer