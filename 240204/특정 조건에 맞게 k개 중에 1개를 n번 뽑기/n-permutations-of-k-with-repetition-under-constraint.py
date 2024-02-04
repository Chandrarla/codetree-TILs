k, n = tuple(map(int, input().split()))
arr = []
ans = []


def choose(curr_n):
    if curr_n > n:
        ans.append(arr[:])
        return

    for i in range(1, k + 1):
        arr.append(i)
        choose(curr_n + 1)
        arr.pop()

choose(1)

def is_diff(arr):
    cnt = 0
    if len(arr) == 1:
        return True
    for elem in arr:
        if elem == arr[0]:
            cnt += 1
    if cnt == n:
        return False
    else: return True

for elem in ans:
    if is_diff(elem):
        for i in elem:
            print(i, end=" ")
        print()