n, m = map(int, input().split())
l = sorted(map(int, input().split()))  # 입력을 정렬하여 사전 순으로 처리
arr = [0] * m
used = set()  # 중복 수열을 추적하기 위한 집합

def nm(i):
    if i == m:
        seq = tuple(arr)  # 현재 수열을 튜플로 변환
        if seq not in used:  # 중복 여부 확인
            used.add(seq)
            print(*arr)
        return
    for j in range(len(l)):
        if i == 0 or arr[i - 1] <= l[j]:  # 비내림차순 조건
            arr[i] = l[j]
            nm(i + 1)

nm(0)
