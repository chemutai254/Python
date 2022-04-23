# Function that checks for prime numbers

def isPrimeNumber(n):
    for num in range(2, n):
        if n % num == 0:
            return False
    return True