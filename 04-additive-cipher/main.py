def encrypt(text, key):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            num = (ord(ch) - ord('A') + key) % 26
            result += chr(num + ord('A'))
        else:
            result += ch
    return result
def decrypt(text, key):
    return encrypt(text, -key)
plain = input("Enter plaintext: ")
key = int(input("Enter key (0-25): "))
cipher = encrypt(plain, key)
print("Cipher text:", cipher)
print("Decrypted  :", decrypt(cipher, key))
