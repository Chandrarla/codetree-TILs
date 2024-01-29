n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def count_consecutive(arr, m):
    global ans
    n = len(arr)

    def count_in_line(line):
        global ans  # 여기에서도 전역 변수 ans 사용 선언
        cnt = 1
        prev = line[0]
        for i in range(1, n):
            if line[i] == prev:
                cnt += 1
                if cnt == m:  # m개의 연속된 같은 숫자를 발견하면 ans 증가
                    ans += 1
            else:
                cnt = 1
                prev = line[i]

    for i in range(n):
        count_in_line(arr[i])

    for j in range(n):
        count_in_line([arr[i][j] for i in range(n)])


count_consecutive(arr, m)
print(ans)