# Python program to check if the input number is prime or not

a=int(raw_input())

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if a > 1:
    # check for factors
    for i in range(2, a):
        if (a % i) == 0:
            print(a, "is not a prime number")
            print(i, "times", a // i, "is", a)
            break
    else:
        print(a, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(a, "is not a prime number")