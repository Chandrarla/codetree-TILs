a, b, c, d = tuple(map(int, input().split()))
A = input()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["NONE", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

month = a
date = b
day = 1
cnt = 0

while True:

    if days[day % 7] == A:
        cnt += 1

    if month == c and date == d:
        print(cnt)
        break

    date += 1
    day += 1

    if date > num_of_days[month]:
        month += 1
        date = 1