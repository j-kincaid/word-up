
def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)


###################
def main():
    print(alphabet_position('This is the Crypto Assignment'))
    print(alphabet_position('nopqr'))
    print(alphabet_position(alphabet_position('since rot thirteen is symmetric you should see this message')))

if __name__ == "__main__":
    main()
