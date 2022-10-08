# Exercise 1: Write a function that takes in two numbers and
# recursively multiplies them together.

def product(a, b):
    """If a less than b swap"""
    if a < b:
        return product(b, a)
    # recursively calculate b times the sum of a
    elif b != 0:
        return a + product(a, b - 1)
    # if both numbers equal zero return zero
    else:
        return 0


# Driver Method
if __name__ == "__main__":
    print(product(5, 10))
