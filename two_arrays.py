array1 = ['a', 'b', 'c', 'd']
array2 = ['x', 'y', 'z', 'a']

def contains_common_item(array1:list, array2:list):
    dict1 = {item: True for item in array1}
    for i in array2:
        res =  dict1.get(i, None) 
        if res:
            return True
    return False

print(contains_common_item(array1, array2))