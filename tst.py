
arr = input().split(" ")
n = int(arr[0])
m = int(arr[1])
a = input()
values = list(map(float, a.split()))
res = n
for i in values:
    j = 1 - i
    res = res//j - 1
print(int(res))