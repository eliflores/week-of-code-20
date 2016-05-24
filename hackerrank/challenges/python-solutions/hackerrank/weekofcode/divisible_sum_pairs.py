param_array = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n = param_array[0]
k = param_array[1]
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

count = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if (arr[i] + arr[j]) % k == 0:
            count += 1

print(count)
