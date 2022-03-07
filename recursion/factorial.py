
def find_factorial_recusive(number): 
    if not isinstance(number, int) or number <= 0:
        return {"err": "Please put a positeve integer."}

    if number == 2:
        return 2
    
    return number * find_factorial_recusive(number - 1)

def find_factorial_iterative(number:int):
    if not isinstance(number, int) or number <= 0:
        return {"err": "Please put a positeve integer."}

    answer = 1
    while number > 1:
        answer *= number
        number -= 1
    return answer

if __name__ == "__main__":
    print(find_factorial_recusive(2))
    # print(find_factorial_iterative(7))