text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
shifted = alphabet[index + shift]

# CAESAR Cipher

# Caesar cipher. Takes each letter in a message, finds its position in the alphabet,
# takes the letter located after 3 positions in the alphabet,
# and replaces the original letter with the new letter

# the .find() method finds the position of the first occurance of a string element.
# A method is similar to a function, but it belongs to an object.
encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char)
    new_index = index+shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)
