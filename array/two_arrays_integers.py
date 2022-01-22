from collections import defaultdict


array1 = [1, 2, 3, 9] # sum = 8 retun False
array2 = [1, 2, 4, 4] # sum = 8 retun True

def find_pair_sum(arr: list, sum: int):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                return True
    return False

print(find_pair_sum(array2, 8))


def find_pair_sum2(arr: list, sum: int):
    complement_set = set()
    for i in arr:
        complement = sum - i
        if i in complement_set:
            return True

        if complement not in complement_set:
            complement_set.add(complement)

    return False

print(find_pair_sum2(array1, 16))


