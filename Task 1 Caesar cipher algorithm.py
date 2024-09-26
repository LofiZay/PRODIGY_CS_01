def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Program")
    text = input("Enter the text required to encrypt or decrypt: ")
    shift = int(input("Enter the shift value (1-25): "))
    mode = input("Type 'encrypt' for encrypting the text or 'decrypt' for decrypting the text: ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    result = caesar_cipher(text, shift, mode)
    print(f"The {mode}ed text is: {result}")

if __name__ == "__main__":
    main()
