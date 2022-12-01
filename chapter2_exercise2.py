# Q1: Ask user name and print back user name in reverse order.
# BONUS: Try to make your program in two lines using string formatting.

name = input("Enter your name: ")
reverse = name[-1::-1]
print(f"Reverse of your name is {reverse}")

#BONUS:
name = input("Enter your name: ")
print(f"Reverse of your name is {name[-1::-1]}")