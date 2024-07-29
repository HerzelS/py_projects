text = 'Hello Zaira'
shift = 3
custom_key = 'python'

#index = alphabet.find(text[0].lower())
#shifted = alphabet[index + shift]

# CAESAR Cipher

# Caesar cipher. Takes each letter in a message, finds its position in the alphabet,
# takes the letter located after 3 positions in the alphabet,
# and replaces the original letter with the new letter
# Weakness, every single letter is always encrypted with the same letter,
# depending on the specified offset.

# the .find() method finds the position of the first occurance of a string element.
# A method is similar to a function, but it belongs to an object.

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Vigenere cipher
# What if the offset were different for each letter?
# That would be much more difficult to decrypt.
# This algorithm is referred to as the Vigenère cipher,
# where the offset for each letter is determined by another text,
# called the key.
def vigenere(message, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha(): # The .isalpha() method returns True if all of 
        #the characters of the string on which it is called are letters.
        # This is ensure none letter characters
            encrypted_text += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted/encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

def encyrpt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)
    



print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')