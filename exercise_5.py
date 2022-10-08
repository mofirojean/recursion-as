# Write a function using recursion that takes in a string and returns a reversed copy of the string.
# The only string operation you are allowed to use is string concatenation.

def reverseString(text: str) -> str:
    # base case for the recursion
    # return the text is the length is zero
    if len(text) == 0:
        return text
    # if the length of the string is not equals to zero
    # then reverseString function is recursively called
    # to slice the part of the string except the first character
    # and concatenate the first character to the end of te sliced string
    else:
        return reverseString(text[1:]) + text[0]


# Driver Method
def main():
    word = "reverse string"
    print(reverseString(word))


if __name__ == "__main__":
    main()
