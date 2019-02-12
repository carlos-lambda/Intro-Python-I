# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# flawed code, returns odd and even on 6 and nothing on 5


def is_even(num):
    if type(num) is int and num % 2 == 0:
        print('is even')
    if type(num) is int and num % 3 == 0 or num == 1:
        print('is odd')
    if type(num) != int:
        print('That is not a number')


is_even(num)
