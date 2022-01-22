# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

from typing import List

test_set = {}
test_set['arr1'] = [2, 5, 5, 2, 3, 5, 1, 2, 4]
test_set['arr2'] = []
test_set['arr3'] = [1]
test_set['arr4'] = [7, 7]


def find_first_recurrent_char(arr1: List[int]):
    records = set()
    for i in arr1:
        if i in records:
            return i
        else:
            records.add(i)
    return None

# time complexity O(N)
# space complexity O(N)


def find_first_recurrent_char2(arr1: List[int]):
    min_j = len(arr1)
    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            if arr1[i] == arr1[j]:
                if j < min_j:
                    min_j = j
    if min_j < len(arr1):
        return arr1[min_j]

    return None


for arr in test_set.values():
    print(find_first_recurrent_char2(arr))
