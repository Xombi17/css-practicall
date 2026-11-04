def encrypt(text):
    even = ""
    odd = ""
    for i in range(len(text)):
        position = i + 1          # 1-based position
        if position % 2 == 0:
            even += text[i]
        else:
            odd += text[i]
    return even + odd

plain = input("Enter plaintext: ")
print("Cipher text:", encrypt(plain))
