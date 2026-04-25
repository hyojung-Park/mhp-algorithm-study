# 문제: 나누어 떨어지는 숫자 배열
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for num in arr:
        if not num%divisor:
            answer.append(num)
    if answer:
        answer.sort()
    else: answer = [-1]
    return answer

# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]