def encrypt(text, shift):
    result = ""
    
    # Traverse through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage with user input
if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print(f"Original: {text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
