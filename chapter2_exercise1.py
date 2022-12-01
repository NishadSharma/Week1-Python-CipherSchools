# Q1: Ask user to input 3 numbers and you have to print the average of three numbers using string formatting.
# Bonus: Try to take all three comma separated inputs in one line.

number1=input("Enter first number: ")
number2=input("Enter second number: ")
number3=input("Enter third number: ")
# Add three numbers and divide it by 3.
print(f"Average of three numbers: {(int(number1) + int(number2) + int(number3)) / 3}")

#Bonus:
number1 , number2 , number3 = input("Enter three numbers comma seperated: ").split(",")
# Add three numbers and divide it by 3.
print(f"Average of three numbers: {(int(number1) + int(number2) + int(number3)) / 3}")