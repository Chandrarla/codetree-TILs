n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

def count_consecutive(arr, m):
    total_count = 0

    def count_in_line(line):
        cnt = 0
        for i in range(1, len(line)):
            if line[i] == line[i-1]:
                cnt += 1
                if cnt == m - 1:
                    return 1
            else:
                cnt = 0
        return 0

    for i in range(n):
        total_count += count_in_line(arr[i])
    for j in range(n):
        total_count += count_in_line([arr[i][j] for i in range(n)])

    return total_count

ans = count_consecutive(arr, m)
print(ans)