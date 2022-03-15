
def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == "__main__":
    arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(selection_sort(arr))