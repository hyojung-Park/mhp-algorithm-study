 # [성능 요약] 메모리: 9.2 MB 시간: 0.13 ms 

def solution(num):
    answer = -1
    
    if num == 1:
        return 0
    
    cnt = 0
    while cnt < 500:
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        
        cnt += 1
        
        if num == 1:
            answer = cnt
            break
    
    return answer