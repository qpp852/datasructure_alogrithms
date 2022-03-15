# def insertion_sort(array):
#     sorted_array = []
#     # sorted_array = [1, 2, 6, 44, 99]
#     for i in range(len(array)):

#         if len(sorted_array) == 0:
#             sorted_array.append(array[i])
#             continue

#         added = False

#         for j in range(len(sorted_array)):
#             if array[i] < sorted_array[j]:
#                 sorted_array.insert(j, array[i])
#                 added = True
#                 break
        
#         if not added:
#             sorted_array.append(array[i])
                
#     return sorted_array

# def insertion_sort(array):
#     length = len(array)
#     for i in range(1, length):
#         key = array[i]
#         j = i - 1
#         while j >= 0 and key < array[j]:
#             array[j+1] = array[j]
#             j -= 1
#         array[j + 1] = key
#     return array


def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        j = i - 1
        while j >= 0 and array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
            j -= 1
            i -= 1
    return array


if __name__ == "__main__":
    arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(insertion_sort(arr))