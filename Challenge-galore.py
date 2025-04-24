def encrypt(message,shift):
    return ''.join(chr(ord(char)+shift)for char in message)

def decrypt(encrypted_message,shift):
    return ''.join(chr(ord(char)-shift)for char in encrypted_message)

encrypted=encrypt("Hey Dude! What's upp:",2)
print("Encrypted message:",encrypted)

decrypted=decrypt(encrypted,2)
print("Decrypted message:",decrypted)