ALPHABET_SIZE = 26

def caesar_shift(character, key):
    if character.isalpha():
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        if character.isupper():
            new_character = alphabet_upper[(alphabet_upper.index(character) + key) % ALPHABET_SIZE]
        else:
            new_character = alphabet_lower[(alphabet_lower.index(character) + key) % ALPHABET_SIZE]
    else:
        new_character = character
    return new_character

def caesar_encrypt(text, key):
    encrypted_text = "".join(caesar_shift(char, key) for char in text)
    return encrypted_text

def caesar_decrypt(encrypted_text, key):
    return caesar_encrypt(encrypted_text, -key)

def main():
    # Get user input
    text = input("Enter the text to encrypt: ")
    try:
        key = int(input("Enter the key for encryption: "))
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    # Encryption
    encrypted_text = caesar_encrypt(text, key)
    print("Encrypted Text:", encrypted_text)

    # Decryption
    decrypted_text = caesar_decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
