# Watch Movie - COCO
# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# Print 'YOU CAN WATCH COCO MOVIE' 
# Else print 'SORRY! YOU CANNOT WATCH COCO MOVIE'

user_name = input("Enter your name please : ")
user_age = input("Enter your age please : ")
user_age = int(user_age)
if user_age >= 10 and (user_name[0]=='a' or user_name[0] == 'A'):
    print("YOU CAN WATCH COCO MOVIE")
else:
    print("SORRY! YOU CANNOT WATCH COCO")