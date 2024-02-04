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

cnt = 0
for elem_arr in ans:
    for elem in elem_arr:
        if elem_arr[0] == elem:
            cnt+=1
    if cnt != n:
        for i in elem_arr:
            print(i, end=" ")
    print()