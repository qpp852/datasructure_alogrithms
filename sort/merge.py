def merge_sort(array):
    if not isinstance(array, list):
        return {'err': 'array shold be a list.'}

    if len(array) == 1:
        return array

    cut_point = int(len(array)/2)
    # print(123, array[:cut_point])

    left = array[:cut_point] # [99, 1]
    right = array[cut_point:] # [3, 7, 9]
    print(left, right)

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    left_index = 0
    right_index = 0
    sorted_array = []
    # print(right, left)

    while left_index < len_left and right_index < len_right:
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1

        else:
            sorted_array.append(right[right_index])
            right_index += 1
    
    if left_index < len_left:
        sorted_array += left[left_index:]

    else:
        sorted_array += right[right_index:]
    
    return sorted_array

if __name__ == "__main__":
    # arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    arr = [99, 1, 3, 7, 9]
    print(merge_sort(arr))