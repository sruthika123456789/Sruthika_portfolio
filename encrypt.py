def encrypt(text, shift):
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + shift)
    return encrypted

message = input("Enter text to encrypt: ")
shift = 2
print("Encrypted text:", encrypt(message, shift))
