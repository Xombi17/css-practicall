def encrypt(text, key):
    result = ""
    for letter in text.upper():
        if "A" <= letter <= "Z":
            result += chr((ord(letter) - 65 + key) % 26 + 65)
        else:
            result += letter
    return result

def decrypt(text, key):
    return encrypt(text, -key)

plaintext = input("Plaintext: ")
key = int(input("Shift key: ")) % 26
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypt(ciphertext, key))
