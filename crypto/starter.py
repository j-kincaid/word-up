def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_index = (alphabet_position(char) + 13) % 26
        if ord(char) > 64 and ord(char) < 90:
            rotated = rotated + alphabet[rotated_index].upper()
        else:
            if ord(char) < 123 and ord(char) > 97:
                rotated = rotated + alphabet[rotated_index]

    return rotated

# print(ord("A")) = 65
# print(ord("Z")) = 90
# print(ord("a")) = 97
# print(ord("z")) = 122


def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_index = (alphabet_position(char) + rot) % 26

    if ord(char) :
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
    rotate_string(text, rot)


if __name__ == "__main__":
    main()