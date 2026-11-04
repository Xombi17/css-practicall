def shift(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result
plain = input("Enter plaintext: ")
key = int(input("Enter shift key: "))
cipher = shift(plain, key)
decrypted = shift(cipher, -key)
print("Cipher text:", cipher)
print("Decrypted  :", decrypted)