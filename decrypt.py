def decrypt(text, shift):
    decrypted = ""
    for char in text:
        decrypted += chr(ord(char) - shift)
    return decrypted

message = input("Enter text to decrypt: ")
shift = 2
print("Decrypted text:", decrypt(message, shift))
