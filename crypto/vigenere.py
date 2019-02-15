from helpers import alphabet_position, rotate_character

def encrypt(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    key_count = 0
    code_len = len(key)
    mess_len = len(message)
    for i in range(code_len):
        if key[i].isalpha() is not True:
            print("Key word must contain only letters")
            break
            
    for char in message:
        if char.isalpha() is not True:
            encrypted = encrypted + char
        else:
            encrypted += rotate_character(char, alphabet_position(key[key_count]))
            if key_count == len(key) - 1:
                key_count = 0
            else:
                key_count += 1
    return encrypted
    
def main():
    # your main code (input and print statements)
    message = input("Type a message:")
    key = input("Encryption key:")
    result = encrypt(message, key)
    print(result)
if __name__ == "__main__":
    main()