# 문제: 콜라츠 추측
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    cnt = 0

    if num == 1:
        return 0

    while cnt <= 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        cnt += 1
        if num == 1:
            break

    if num != 1:
        return -1

    return cnt