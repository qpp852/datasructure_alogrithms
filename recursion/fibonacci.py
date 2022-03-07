# Given a number N return the index value of Fibonacci sequence,
# where the sequence is :
# 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

def find_fibonacci_recusive(n):
    if not isinstance(n, int) or n <= 0:
        return {"err": "Please put a positeve integer."}

    if n == 1:
        return 0
    
    if n == 2:
        return 1

    return find_fibonacci_recusive(n - 1) + find_fibonacci_recusive(n - 2)

def find_fibonacci_iterative(n):
    if not isinstance(n, int) or n <= 0:
        return {"err": "Please put a positeve integer."}

    if n == 1:
        return 0
    
    if n == 2:
        return 1

    previous = 0
    current = 1
    next = 1
    for i in range(n-3):
        previous = current
        current = next
        next = current + previous

    return next
        

if __name__ == "__main__":
    import time
    n = 445

    s = time.time()
    # print(find_fibonacci_recusive(n))
    print(find_fibonacci_iterative(n))
    e = time.time()
    
    print(e - s)
    