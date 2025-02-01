# Fibonacci Sequence 
i = 0 
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a]
    for i in range(n - 1):
        a, b = b, a + b
        fib_sequence += [a]
    return fib_sequence

# Print the first 10 numbers in the Fibonacci sequence
print(fibonacci(10))