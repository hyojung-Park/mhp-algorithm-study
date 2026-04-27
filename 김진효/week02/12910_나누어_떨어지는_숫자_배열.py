 # [성능 요약] 메모리: 12.2 MB 시간: 17.71 ms 

# # 정렬 먼저
# def solution(arr, divisor):
#     answer = []
    
#     arr.sort()
    
#     for n in arr:
#         if n % divisor == 0:
#             answer.append(n)
            
#     if len(answer) == 0:
#         answer.append(-1)
    
#     return answer

 # [성능 요약] 메모리: 12.3 MB 시간: 4.85 ms 
# 이후에 정렬이 더 빠를 것 같다
def solution(arr, divisor):
    answer = []
    
    for n in arr:
        if n % divisor == 0:
            answer.append(n)
            
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
        
    return answer