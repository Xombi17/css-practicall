def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def encrypt(text, a, b):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - ord('A')
            result += chr((a*p + b) % 26 + ord('A'))
        else:
            result += ch
    return result
def decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            c = ord(ch) - ord('A')
            result += chr((a_inv * (c - b)) % 26 + ord('A'))
        else:
            result += ch
    return result
plain = input("Enter plaintext: ")
a = int(input("Enter key a (coprime with 26, e.g. 5): "))
b = int(input("Enter key b (e.g. 8): "))
cipher = encrypt(plain, a, b)
print("Cipher text:", cipher)
print("Decrypted  :", decrypt(cipher, a, b))
