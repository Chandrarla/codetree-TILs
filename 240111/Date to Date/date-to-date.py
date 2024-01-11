a, b, c, d = tuple(map(int, input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = 0, 0

for i in range(1, a+1):
    x += num_of_days[i]

for j in range(1, c+1):
    y += num_of_days[j]

print((y+d) - (x+b) + 1)