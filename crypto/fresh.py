def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_index = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_index].upper()
        else:
            rotated = rotated + alphabet[rotated_index]

    return rotated

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_index = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_index].upper()
    else:
        return alphabet[rotated_index]

def rotate_string(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated


def main():
    # your main code (input and print statements)

    text = input("Type a message: ")
    rot = int(input("Rotate by:"))
    result = rotate_string(text, rot)
    print(result)


if __name__ == "__main__":
    main()