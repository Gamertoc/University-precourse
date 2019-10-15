def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_it(n):
    result = 1
    high = 0
    for i in range(n-1):
        x = result
        result += high
        high = x
    return result
        
