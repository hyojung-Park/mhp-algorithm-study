# 문제: 정수 내림차순으로 배치하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    large_list = []
    for i in str(n):
        large_list.append(int(i))
    large_list.sort(reverse=True)
    answer = str()
    for i in large_list:
        answer += str(i)
        answer = str(answer)
        
    return int(answer)