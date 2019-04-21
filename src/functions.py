# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# flawed code, returns odd and even on 6 and nothing on 5


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

is_even = is_even(num)
if is_even == True:
    print("it's even bruhh")
else:
    print("It's odd bruhh")
