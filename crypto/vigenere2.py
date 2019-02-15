def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_index = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_index].upper()
    else:
        return alphabet[rotated_index]

def encrypt(message, key):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    
    code_len = len(key)
    mess_len = len(message)
    for i in range(code_len):
        if key[i].isalpha() is not True:
            print("Key word must contain only letters")
            break

        
        for key, char in enumerate(message):
            if char == ' ':
                encrypted = encrypted + ' '
            else:
                encrypted = rotate_character(char, key)
                return encrypted
                
def main():

    # your main code (input and print statements)
    message = input("Type a message:")
    key = input("Encryption key:")
    result = encrypt(message, key)
    print(result)


if __name__ == "__main__":
    main()