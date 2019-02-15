from helpers import alphabet_position, rotate_character

def encrypt(text, rot):

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
    rot = int(input("Rotate by number:"))
    result = encrypt(text, rot)
    print(result)


if __name__ == "__main__":
    main()
