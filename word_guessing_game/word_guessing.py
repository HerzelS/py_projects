import random
# library that we use in order to chose
# on random words from  list of words

name = input("What is your name? ")

# Here the user is asked to enter the name first.

print(f"Good luck {name}!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


# Function will choose one random
# word from list of words
word = random.choice(words)
print(word)

print("Guess the characters!")

guesses = ""

turns = 12

while turns > 0:
    # count the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:
        # comparing that character with
        # the character in guesses.
        if char in guesses:
            print(char, end="")
        else:
            print("_")

            # for every failure 1 will be
            # incremented to failed
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and "You Win" will be given as output
        print("You Win!")

        # this prints the correct word
        print("The word is", word)
        break

    # if the user has input the wrong alphabte then it will
    # ask the user to enter another alphabet
    print()
    guess = input("guess the character: ")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:
        turns -= 1

        # if the character doesn't match the word
        # then "Wrong" will be given as output
        print("Wrong")

        # this will print the number of
        # turns left for the user.
        print("You have", + turns, "more gueses left.")

        if turns == 0:
            print("You loose!")
            print(f"The word was, {word}")