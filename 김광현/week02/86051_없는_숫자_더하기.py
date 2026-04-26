# 문제: 없는 숫자 더하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = 0
    for i in numbers:
        for j in range(10):
            if i == j:
                answer += i
    answer = 45 - answer
    return answer