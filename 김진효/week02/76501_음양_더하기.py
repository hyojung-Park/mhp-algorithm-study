 # [성능 요약] 메모리: 9.21 MB 시간: 0.15 ms 

def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i
                                ]
    return answer