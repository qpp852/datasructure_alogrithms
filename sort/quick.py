# step1 : assign a pivot (ex: last one of an array)
# step2 : compare pivot with other elements.
# step3 : if pivot is smaller than compared item,
#         compared item is shifted to right hand side of pivot.
#         else, continue.
# step4 : elements on the right hand side of pivot are called right,
#         and elements on the left hand side of pivot are called left.
# step5 : repeat step1 to step4

def quick_sort(array, left, right):
    if left >= right:
        return 
    i = left
    j = right
    key = array[left]

    while i != j:
        # print(i, j)
        # print(array)
        while array[j] >= key and i < j:
            j -= 1
        while array[i] <= key and i < j:
            i += 1
        if i < j: 
            array[i], array[j] = array[j], array[i]

    array[left], array[j] = array[j], array[left]
    

    quick_sort(array, left, i-1)
    quick_sort(array, i+1, right)
    return array


if __name__ == "__main__":
    arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    print(quick_sort(arr, 0, len(arr) - 1))
