
def swaps(array):
    move_steps = 0
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            array[i + 1], array[i] = array[i], array[i + 1]
            move_steps += 1
            
    return (array, move_steps)


def bubble_sort(array):
    while True:
        array, move_steps = swaps(array)
        if move_steps == 0:
            break
        
    return array



if __name__ == "__main__":
    arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(bubble_sort(arr))