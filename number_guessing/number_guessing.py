import random
import math

# Algorithm
# User inputs the lower and upper bounds
# The compute generarates a random integer between the range and store it in a variable for future refrences
# Fore repetitive guessing, a while loop will be initialised
# If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
# Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
# And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
# Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.


# taking inputs
lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))

# Generating random number between
# the lower and upper
number = random.randint(lower, upper)

# Minimum number of guessing = log2(Upper bound – lower bound + 1)
total_chances = math.ceil(math.log(upper-lower +1, 2))
print("\tYou've only", total_chances, "chances to guess the integer!\n")

# Initialising the number of guesses
count = 0
flag = False

# For calculation of minimum number
# of guesses depends upon range
while count < total_chances:
    count += 1

    # taking guessing number as inputs
    guess = int(input("Guess the number: "))

    # Condition testing
    if number == guess:
        print("Congradulations you did it in ", count, "try(s)")
        # Once guessed correct, the loop will break
        flag = True
        break
    elif number > guess:
        print("You guessed too low!")
    elif number < guess:
        print("You guessed too high!")

# If guessing is more than required guesses,
# show this output
if not flag:
    print("\ntHE NUMBER IS %d" % number)
    print("\tBetter Luck next time!")
