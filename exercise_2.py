# Write a function that takes in a base and an exp and recursively computes base exp .
# You are not allowed to use the ** operator!

def power(base, exp):
    # if exp is 0 return 1
    if exp == 0:
        return 1
    # if exp is 1 return the base
    if exp == 1:
        return base
    # recursively multiply base by itself based on the exp
    if exp > 1:
        return base * power(base, exp - 1)
    # if exp is < 0
    # make the exp positive and recursively calculate the power
    # then return 1 divided by the power
    if exp < 0:
        val = -1 * exp
        return 1 / (base * power(base, val - 1))


# Driver Method
def main():
    print("Exponential cases")
    print(f"Case 1: zero exponential\npower(4,0) = {power(4, 0)}")
    print(f"Case 2: negative exponential\npower(4,-2) = {power(4, -2)}")
    print(f"Case 3: exponential equals 1\npower(4,1) = {power(4, 1)}")
    print(f"Case 4: exponential greater than 1\npower(4,3) = {power(4, 3)}")


if __name__ == "__main__":
    main()
