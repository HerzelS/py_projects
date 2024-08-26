import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(" ")
word = random.choice(someWords)

if __name__ == "__main__":
    print("_", end=" ")
print()

playing = True
letter_guessed = ""
chances = len(word) + 2
correct = 0
flag = 0

try:
    while (chances != 0) and flag == 0: # flag is updated when the word is correctly guessed
        print()
        chances -= 1
        try:
            guess = str(input("Enter a letter to guess: "))
        except:
            print("Enter only a letter!")
            continue

        # Validation of the guess
        if not guess.isalpha():
            print("Enter only a LETTER")
            continue
        elif len(guess) > 1:
            print("Enter only a single letter")
            continue
        elif guess in letter_guessed:
            print("You have already guessed that letter")
            continue

        #if letter is guessed correctly
        if guess in word:
            # k stores the number of times the guessed letter occurs in the word
            k = word.count(guess)
            for _ in range(k):
                letter_guessed += guess # the guessed letter is added as many times as it occurs

        # print the word
        for char in word:
            if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
                print(char, end=" ")
                correct += 1

            # if the use has guessed all the letters
            # Once the corrent word is guessed fully.
            elif (Counter(letter_guessed) == Counter(word)):
                # the game ends, even if chances remain
                print("The word is: ", end=" ")
                print(word)
                flag = 1
                print("Congradulations, You Won!")
                break # to break out of the for loop
                break # to break out of the while loop
            else:
                print("_", end=" ")

        # if user used all their chances
        if chances <= 0 and (Counter(letter_guessed) != Counter(word)):
            print()
            print("You lost! Try again...")
            print("The word was {} ".format(word))

except KeyboardInterrupt:
    print()
    print("Bye! Try agin.")
    exit()