def solution(arr):
    n = 0
    for i in range(len(arr)):
        n += arr[i]

    return n / len(arr)