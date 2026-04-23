# 문제: 자연수 뒤집어 배열로 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    for i in range(len(str(n)) -1, -1, -1):
        answer.append(int(str(n)[i]))
    return answer