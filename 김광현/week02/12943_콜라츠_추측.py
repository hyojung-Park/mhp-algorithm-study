# 문제: 콜라츠 추측
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    for _ in range(500):
        if num == 1:
            return answer
        elif num % 2 == 0:
            answer += 1
            num = num // 2
        elif num % 2 != 0:
            answer += 1
            num = num * 3 + 1
    return -1