n = int(input())
arr = [0] * 100
segments = [tuple(map(int, input().split()))
       for _ in range(n)]
for a, b in segments:
    for i in range(a, b):
        arr[i] += 1
max_index = max(arr)
print(max_index)