def inverse(a, m):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
def cipher(text, key, decrypt=False):
    result = ""
    if decrypt:
        key = inverse(key, 26)
    for ch in text.upper():
        if ch.isalpha():
            num = ord(ch) - 65
            result += chr((num * key) % 26 + 65)
        else:
            result += ch
    return result
plain = input("Enter plaintext: ")
key = int(input("Enter key (coprime with 26): "))
encrypted = cipher(plain, key)
print("Cipher text:", encrypted)
decrypted = cipher(encrypted, key, True)
print("Decrypted  :", decrypted)