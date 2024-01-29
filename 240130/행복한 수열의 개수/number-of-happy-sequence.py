n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def check_row(arr):
    global ans
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                if cnt >= m:
                    ans += 1
                    break
            else:
                cnt = 1

def check_column(arr):
    global ans
    for k in range(n):
        cnt = 1
        for l in range(1, n):
            if arr[l][k] == arr[l-1][k]:
                cnt += 1
                if cnt >= m:
                    ans += 1
                    break
            else:
                cnt = 1

check_row(arr)
check_column(arr)
print(ans)