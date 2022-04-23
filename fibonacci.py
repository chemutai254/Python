# Function that checks whether the number belongs to a Fibonacci sequence or not
import math


def is_fibonacci(n):
    fib = 0.5 + 0.5 * math.sqrt(5.0)
    i = fib * n
    return n == 0 or abs(round(i) - i) < 1.0 / n
