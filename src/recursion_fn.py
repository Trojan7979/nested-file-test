# implementing Fibonacci Series

def fibonacci_iterative(n):
    # Generate Fibonacci series up to n terms iteratively
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci_iterative(4)