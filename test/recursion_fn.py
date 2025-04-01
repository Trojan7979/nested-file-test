# implementing factorial fn.

def factorial_iterative(n):
    """Calculate factorial iteratively"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial_iterative(5))