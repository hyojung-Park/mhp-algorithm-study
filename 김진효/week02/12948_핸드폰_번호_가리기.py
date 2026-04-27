 # [성능 요약] 메모리: 9.07 MB 시간: 0.00 ms 

def solution(phone_number):
    answer = ''
    l = len(phone_number)
    answer = '*' * (l - 4) + phone_number[l-4:]
    
    return answer