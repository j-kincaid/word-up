def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower) #_ 1. char from input string 

# alphabet_position(letter), which receives a letter (that is, a string with only one alphabetic character) and returns the 0-based numerical position of that letter within the alphabet.

def rotate_character(char, key, key_cnt):
    if key[key_cnt].islower():
        key_pos = alphabet_position(key[key_cnt]) - alphabet_position('a')
    else:
        key_pos = alphabet_position(key[key_cnt]) - alphabet_position('A')
    if (char.islower()):
        rotated_index = alphabet_position('a') + ((alphabet_position(char) + key_pos - alphabet_position('a')) % 26)
    else:
        rotated_index = alphabet_position('A') + ((alphabet_position(char) + key_pos - alphabet_position('A')) % 26)
        return rotated_index
# rotate_character(char, rot) which receives a character char (that is, a string of length 1), and an integer rot. Your function should return a new string of length 1, the result of rotating char by rot number of places to the right.


def encrypt(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    code_len = len(key)
    mess_len = len(message)
    for i in range(code_len):
        if key[i].isalpha() is not True:
            print("Key word must contain only letters")
            break
            
        key_cnt = 0
        for char in message:
            if char == ' ':
                encrypted = encrypted + ' '
            else:
                index = rotate_character(char, key, key_cnt)
#        return encrypted                               
    
# Write one more function called encrypt(text, rot), which receives as input a string and an integer. Your function should return the result of rotating each letter in the text by rot places to the right.  The text argument might contain non-alphabetic characters (spaces, numbers, symbols). You should leave these as they are.

def main():

    # your main code (input and print statements)
    message = input("Type a message:")
    key = input("Encryption key:")
    result = encrypt(message, key)
    print(result)


if __name__ == "__main__":
    main()