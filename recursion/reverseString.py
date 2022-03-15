
def reverse_string_recursive(string:str):
    if string == '':
        return ''
    
    return reverse_string_recursive(string[1:]) + string[0]

def reverse_string_iterative(string:str):
    array = []
    for i in range(len(string) - 1, -1, -1):
        array.append(string[i])
    return ''.join(array)


if __name__ == "__main__":
    string = 'ABCDE' 
    print(reverse_string_iterative(string))