# Ask a user for name.
# Example - Nishad Sharma
# print count of each words
# Output:
        # N : 1
        # i : 2
        # s : 3
        # h : 2
        # a : 3
        # d : 1
        #   : 1
        # S : 1
        # r : 1
        # m : 1

name = input("Enter your name ")
temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1