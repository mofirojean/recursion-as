# Exercise 4: Write a function using recursion to print numbers from 0 to n

def printInAsc(n):
    if n >= 0:
        printInAsc(n - 1)
        print(n)


# Driver Method
if __name__ == "__main__":
    printInAsc(10)
