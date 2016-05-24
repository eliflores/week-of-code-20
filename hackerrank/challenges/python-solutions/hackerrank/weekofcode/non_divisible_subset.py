def build_non_divisible_tuples(array_of_numbers):
    divisible_dict = {}
    for value in array_of_numbers:
        divisible_dict[value] = 0
        
    for i in range(0, n):
        for j in range(i + 1, n):
            if (array_of_numbers[i] + array_of_numbers[j]) % k == 0:
                divisible_dict[array_of_numbers[i]] = divisible_dict.get(array_of_numbers[i]) + 1
                divisible_dict[array_of_numbers[j]] = divisible_dict.get(array_of_numbers[j]) + 1
    return sorted(divisible_dict.items(), key=lambda x: x[1])


def is_non_divisible(number_to_test, current_subset):
    for number_in_set in current_subset:
        if (number_to_test + number_in_set) % k == 0:
            return False
    return True


param_array = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n = param_array[0]
k = param_array[1]
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

sorted_non_divisible_tuples = build_non_divisible_tuples(arr)
non_divisible_subset = set()

for divisible_tuple in sorted_non_divisible_tuples:
    number = divisible_tuple[0]
    if is_non_divisible(number, non_divisible_subset):
        non_divisible_subset.add(number)

print(len(non_divisible_subset))
