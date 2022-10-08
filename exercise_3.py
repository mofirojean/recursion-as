# Exercise 3: Write a function using recursion to print numbers from n to 0.

def printReverse(n):
    if n >= 0:
        print(n)
        printReverse(n - 1)


# Driver method
if __name__ == "__main__":
    printReverse(10)
