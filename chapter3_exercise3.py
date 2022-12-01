# Exercise one of three.
# Sum of n natural numbers.
# Ask a user for natural number(n).
# Print total from 1 to n.

n = input("Enter a number: ")
n = int(n)
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)