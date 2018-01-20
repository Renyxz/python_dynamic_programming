# Find nth Fibonacci number

# METHOD 1 - RECURSION
def fib_rec(n):
    if n <= 2:
        result = 1
    else:
        result = fib_rec(n - 1) + fib_rec(n - 2)
    
    return result

print(fib_rec(35)) 
# This took about 9 seconds to exit.



# METHOD 2 - MEMOIZATION
def fib_memo(n, memo):
    if memo[n] != None:
        return memo[n]

    elif n <= 2:
        result = 1

    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    
    memo[n] = result

    return result



def fib(n):
    memo = [None] * (n + 1)
    result = fib_memo(n, memo)

    return result


print(fib(998))
# Any number larger than this you cause RecursionError of maximum resursion depth exceeded in comparison.abs



# METHOD 3 - BOTTOM UP 
def fib_bottom_up(n):
    if n <= 2:
        result = 1
    
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    
    return bottom_up[n]

print(fib_bottom_up(10000))
# This exited in around 0.2s
