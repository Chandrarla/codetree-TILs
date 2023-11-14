n, k, T = list(input().split())
arr = []
sorted_arr=[]
for _ in range(int(n)):
    arr.append(input())

for i in range(int(n)):
    if T in arr[i]:
        sorted_arr.append(arr[i])
sorted_arr.sort()

k = int(k)
print(sorted_arr[k-1])