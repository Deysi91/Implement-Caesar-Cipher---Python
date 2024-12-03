# Function to encrypt the message using Caesar Cipher
def encrypt(text, shift):
    result = ''
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, just add the character as is
        else:
            result += char
    return result

# Function to decrypt the message using Caesar Cipher
def decrypt(text, shift):
    result = ''
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # If it's not a letter, just add the character as is
        else:
            result += char
    return result

# Main function to interact with the user
def main():
    print("Caesar Cipher Encryption/Decryption")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt or (Q)uit? ").lower()
        
        if choice == 'e':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        
        elif choice == 'd':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted text: {decrypted_text}")
        
        elif choice == 'q':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select (E) to encrypt, (D) to decrypt, or (Q) to quit.")

if __name__ == '__main__':
    main()
