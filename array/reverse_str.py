str1 = 'abcd'

def reverse_string(string:str):
    col = []
    for i in range(len(string) - 1, -1, -1):
        col.append(str(string[i]))
    return ''.join(col)

print(reverse_string(str1))

