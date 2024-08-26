import random

# list of words
words = ['pyhton', 'java', 'kotlin', 'javascript']

# choose aa random word
word = random.choice(words)
guessed_word = ['_'] * len(word)
attempts = 6

while attempts > 0 and "".join(guessed_word) != word:
    print(" ".join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess

    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")

if "".join(guessed_word) == word:
    print(f"Congradulations! You guessed the word: {word}")

else:
    print(f"Sorry, you ran out of attempts. The word was: {word}.")