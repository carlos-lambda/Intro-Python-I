"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt') as f:
    read_data = f.read()
    print(read_data)
    f.closed
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
b = open('bar.txt', "w")

lines = ['This is my first line\n',
         'This is my second line\n', 'This is my third line']
for i in lines:
    b.write(i)

with open('bar.txt') as b:
    read_data = b.read()
    print(read_data)
    b.closed
