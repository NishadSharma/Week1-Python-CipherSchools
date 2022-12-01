# Q1: Take two comma seperated inputs from user.
# a.) User's name.
# b.) A single character.

# Output - 2 print lines
# a.) User's name length.
# b.) Count the character that user inputed (BONUS : Case insensitive count)

name, char = input("Enter coma seperated name and character: ").split(",")
print(f"Length of your name is {len(name)}")
print(f"character count: {name.count(char)}")

#BONUS:
name, char = input("Enter coma seperated name and character: ").split(",")
print(f"Length of your name is {len(name)}")
print(f"character count: {name.lower().count(char.lower())}")