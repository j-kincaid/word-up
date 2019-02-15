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

    rotated = ''

    for char in message:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, message)
        else:
            rotated = rotated + char

    return rotated

def main():
    # your main code (input and print statements)
    
    message = input("Type a message:")
    key = input("Encryption key:")
    result = encrypt(message, key)
    print(result)


if __name__ == "__main__":
    main()

