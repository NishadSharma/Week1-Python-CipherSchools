name = "James"
print(name.center(11,'*'))
print(name.center(8,'*'))
print(name.center(9,'*'))


name = str(input("enter your name:"))
length = len(name)
print(name.center(length+8,"*"))

string="string"
string[1]="S"                            #cannot give output because string are immutable
print(string.replace("s","S"))           #stored in new 
print(string)