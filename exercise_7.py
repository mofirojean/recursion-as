"""
    Exercise 7:
    Write a recursive function that takes in one argument n and computes F n ,
    the n th value of the Fibonacci sequence.
    Recall that the Fibonacci sequence is defined by the relation.

    F n = F n−1 + F n−2
    where  F 0 = 0 and F 1 = 1
"""


def fib(n):
    if n >= 1:
        if n < 3:
            return n - 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return "Fibonacci not defined for n < 1"


# Driver Method
if __name__ == "__main__":
    print(fib(11))
