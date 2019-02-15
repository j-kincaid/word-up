def alphabet_position(character):
    for char in alphabet:
        a = ord(char)
        if ( a > 64 and a < 91):
    else:
        if ( a > 96 and a < 123):
    return alphabet.index(key, message)

def rotate_character(message, key):
    for char in message:
        a = ord(char)
        rotated_index = (a + key) % 26
        if (a > 64 and a < 91):
            return a[rotated_index]
        else:
            if (a > 96 and a < 123):
                return a[rotated_index]

##################### TEST #################
###__________________        ________________

# def upper_lower(character);
#     for char in text:
#         a = ord(char)
#         if ( a > 64 and a < 91):
#     else:
#         if ( a > 96 and a < 123):
#     return a

# def key_index():
#     kdx = ""
#     for char in key:
#         char = char + char[0]
#     return kdx




# def rotate_string(text, rot):

#     rotated = ''

#     for char in text:
#         if (char.isalpha()):
#             rotated = rotated + rotate_character(char, rot)
#         else:
#             rotated = rotated + char

#     return rotated

# ###__________________        ________________
# def rotate_string(text, rot):

#     rotated = ''

#     for char in text:
#         if (char.isalpha()):
#             rotated = rotated + rotate_character(char, rot)
#         else:
#             rotated = rotated + char

#     return rotated
# ###__________________        ________________
# ##################### TEST #################

def rotate_character(message, key):
    for char in message:
        a = ord(char)
        rotated_index = (a + rot) % 26
        if (a > 64 and a < 91):
            return a[rotated_index]
        else:
            if (a > 96 and a < 123):
                return a[rotated_index]

def encrypt(key, message):
    key = input("Encryption key:")
    message = input("Type a message:")
    

def main():
    # your main code (input and print statements)

    key = input("Encryption key:")
    message = input("Type a message:")
    result = rotate_character(message, key)
    print(result)


if __name__ == "__main__":
    main()

