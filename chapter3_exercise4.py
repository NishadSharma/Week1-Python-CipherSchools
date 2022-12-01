# Problem...
# Ask user to input a number containing more than one digit.
# Example - 1234
# Calculate 1+2+3+4 and print.

# Algorith - (Method to solve problem in human language)
# Ask input in string, i.e. don't change string to int.
# Example - "1234"
# Pick string character one by one and change to int.
# int(example[0]) + int(example[1])...go upto len(example).

number = input("Enter a number ")
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)