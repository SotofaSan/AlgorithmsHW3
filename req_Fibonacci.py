# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2

# Fibonacci sequence 0 1 1 2 3 5 8 13 21 34 55 89
# find the Fn:

def fibonacci(n):
    fib0 = 0
    fib1 = 1

    if n == 0:
        return fib0
    if n == 1:
        return fib1
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(11))