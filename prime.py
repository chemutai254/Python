# Function that checks whether a number is a prime number or not


num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("\n", num, "is not a prime number")
            break
        else:
            print("\n", num, "is a prime number")
else:
    print("\n", num, "is not a prime number")
