# 문제: 서울에서 김서방 찾기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f'김서방은 {i}에 있다'