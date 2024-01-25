n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def get_count(row_s, row_e, col_s, col_e):
    coin_num = 0
    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            coin_num += arr[row][col]
    return coin_num


max_coin = 0
for row in range(n):
    for col in range(n):
        # if row + 3 >= n or col + 3 >= n:
        #     continue
        #
        # coin_num = get_count(row, row + 2, col, col + 2)
        if row + 2 < n and col + 2 < n:  # Adjusted the condition
            coin_num = get_count(row, row + 2, col, col + 2)
            max_coin = max(max_coin, coin_num)
        max_coin = max(max_coin, coin_num)

print(max_coin)