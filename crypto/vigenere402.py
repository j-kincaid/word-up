def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)


# def rotate_character(char, rot):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     rotated_index = (alphabet_position(char) + rot) % 26

#     if char.isupper():
#         return alphabet[rotated_index].upper()
#     else:
#         return alphabet[rotated_index]


    # So we are dealing with each character in the message, each character 
    # in the key, and then the message is the function that calls the other 
    # functions. Before we had text and rot but now we have a message_char, 
    # # a key_char, and a rotation amount.
    # message = "Hi Jessica"
    # key = "Hello"
    #     encrypted message = "H+H i+e J+l e+l s+o s+H i+e c+l a+l "
    # message always starts as 0. it is a counter to count the no. of keys. and it is incremented.
    # Do: put message = 0 at the start of the for loop.

def rotate_character(char, key, key_cnt):    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    key_pos = 0
    for char in message:
        if key[key_cnt].islower():
            key_pos = alphabet_position(key[key_cnt]) - alphabet_position('a')
        else:
            key_pos = alphabet_position(key[key_cnt]) - alphabet_position('A')
        if (char.islower()):
            rotated_index = alphabet_position('a') + ((alphabet_position(char) + key_pos - alphabet_position('a')) % 26)
        else:
            rotated_index = alphabet_position('A') + ((alphabet_position(char) + key_pos - alphabet_position('A')) % 26)
        return rotated_index

def encrypt(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in message:
        if char == '':
            encrypted = encrypted + ''
        else:
            key_pos = alphabet.index(char)
            encrypted = encrypted + key_pos
    return encrypted
    
    # 
    #    # If the character that is the index in the string called message
    #    # is lower case: 
    #    # then that character is the same number of places from [0] in the
    #    lowercase range 
       # or if it's upper case, then the character is that far from [0] in the
       # uppercase range
       # if the character from the message is lowercase:
       # Here we use the key_pos value to index the character from the message
       # same if the character from the message is uppercase:

def main():
    # your main code (input and print statements)
    
    message = input("Type a message:")
    key = input("Encryption key:")
    result = encrypt(message, key)
    print(result)


if __name__ == "__main__":
    main()