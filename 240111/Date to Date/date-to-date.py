a, b, c, d = tuple(map(int, input().split()))
// 1 28 3 24
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = 0, 0

for i in range(a):
    x += num_of_days[i]

for j in range(c):
    y += num_of_days[j]
if x==y:
    print(1)
else:print((y+d) - (x+b))