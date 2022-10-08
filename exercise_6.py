# Exercise 6: Write a function using recursion to check if a number n is prime
# (you have to check whether n is divisible by any number below n).

def isPrime(n, i=2):
    # check is the numbers equals 2
    if n == i:
        return True
    # Checks if the number is divisible by numbers less than itself
    elif n % i == 0:
        return False
    # recursively call the isPrime function to evaluate the
    # conditions above until the base case is reached
    else:
        return isPrime(n, i + 1)


# Driver Method
def main():
    print("is 3 a prime number:", isPrime(3))
    print("is 4 a prime number:", isPrime(4))
    print("is 5 a prime number:", isPrime(5))
    print("is 6 a prime number:", isPrime(6))
    print("is 7 a prime number:", isPrime(7))
    print("is 29 a prime number:", isPrime(29))


if __name__ == "__main__":
    main()
