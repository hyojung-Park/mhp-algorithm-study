# 문제: 나누어 떨어지는 숫자 배열
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]