def vigenere(text, keyword, decrypt=False):
    result = ""
    keyword = keyword.upper()
    j = 0
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - 65
            k = ord(keyword[j % len(keyword)]) - 65
            if decrypt:
                value = (p - k) % 26
            else:
                value = (p + k) % 26

            result += chr(value + 65)
            j += 1
        else:
            result += ch

    return result

plain = input("Enter plaintext: ")
keyword = input("Enter keyword: ")
cipher = vigenere(plain, keyword)
print("Cipher text:", cipher)
decrypted = vigenere(cipher, keyword, True)
print("Decrypted  :", decrypted)