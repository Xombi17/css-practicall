def encrypt(text, key):
    result = ""
    for letter in text.upper():
        if "A" <= letter <= "Z":
            value = ord(letter) - 65
            result += chr((value + key) % 26 + 65)
        else:
            result += letter
    return result

def decrypt(text, key):
    return encrypt(text, -key)

plaintext = input("Plaintext: ")
key = int(input("Additive key: ")) % 26
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypt(ciphertext, key))
