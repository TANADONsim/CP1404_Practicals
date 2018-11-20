"""
1. Write a program that asks the user for their name, then opens a file called “name.txt” and writes that
name to it.
2. Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
3. Create a text file called “numbers.txt” (You can create a simple text file in PyCharm with Ctrl+N, choose
“File” and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
result, which should be… 59.
4. Extended (perhaps only do this if you’re cruising… if you are struggling, just read the solution) …
Now extend your program so that it can print the total for a file containing any number of numbers.
"""


out_file = open("name.txt", "w")
name = input("Please enter your name:")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
print("Your name is", in_file.read())
in_file.close()


in_file = open("numbers.txt", "r")
numbers = []
for number in in_file.read().split():
    numbers.append(int(number))
print("The sum is {}".format(sum(numbers)))
in_file.close()
