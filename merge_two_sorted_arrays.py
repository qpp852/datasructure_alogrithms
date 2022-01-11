# input 2 sorted arrays
# output 1 sorted array
# arrays contains positive integers
# output arrays include repetive elements

array1 = [0, 3, 4, 31, 90, 110]
array2 = [4, 6, 30, 75, 95, 120, 135]

def merge_sorted_arrays(arr1:list, arr2:list):
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        print('Input should be list.')
    
    merged_sorted_array = []

    arr1_index = 0
    arr2_index = 0

    arr1_max_index = len(arr1) - 1
    arr2_max_index = len(arr2) - 1

    while arr1_index <= arr1_max_index or arr2_index <= arr2_max_index:
        if arr1[arr1_index] <= arr2[arr2_index]:
            merged_sorted_array.append(arr1[arr1_index])

            if arr1_index == arr1_max_index:
                merged_sorted_array += arr2[arr2_index:]
                arr2_index = arr2_max_index
                break
            else:
                arr1_index += 1

        elif arr1[arr1_index] > arr2[arr2_index]:
            merged_sorted_array.append(arr2[arr2_index])

            if arr2_index == arr2_max_index:
                merged_sorted_array += arr1[arr1_index:]
                arr1_index = arr1_max_index
                break
            else:
                arr2_index += 1

    return merged_sorted_array
            

print(merge_sorted_arrays(array1, array2))