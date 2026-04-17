def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "Hello, World!"
    shift_value = 3
    
    encrypted = caesar_cipher(message, shift_value, 'encrypt')
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    
    decrypted = caesar_cipher(encrypted, shift_value, 'decrypt')
    print(f"Decrypted: {decrypted}")
