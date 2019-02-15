def rot_n(mess, rotated_index):
    mess = input("This is the Crypto Assignment:")
    rotated_index = int(input("Rotate by:"))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in mess:
        if char == ' ':
            rotated = encrypted + ' '
        else:
            rotated_index = alphabet.index(char) + 26
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted

def main():
    print(rot_n('abcde'))
    print(rot_n('nopqr'))
    print(rot_n(rot_n('If your rotated index is symmetric you should see this message')))

if __name__ == "__main__":
    main()
