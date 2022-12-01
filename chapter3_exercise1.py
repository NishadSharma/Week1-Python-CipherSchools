# Q1: Exercise , Number Guessing game.
# Make a varriable, like winning_number and assign any number to it.
# Ask user to guess a number.
# If user guessed correctly then print "YOU WIN !!!".
# If user didn't guessed correctly then:
   # If user guessed lower than actual number then print "too low"
   # If user guessed higher than actual number then print "too high"

# Google "how to generate random number in python " to generate random.
# Winning number. 
 
winning_number = 7
user_input = input("Guess a number between 1 and 10: ")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN !!!")
else:
    if user_input < winning_number:
        print("Too Low")
    else:
        print("Too High")