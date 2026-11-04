def encrypt(text, keyword):
    result = ""
    key_position = 0
    for letter in text.upper():
        if "A" <= letter <= "Z":
            shift = ord(keyword[key_position % len(keyword)]) - 65
            result += chr((ord(letter) - 65 + shift) % 26 + 65)
            key_position += 1
        else:
            result += letter
    return result

def decrypt(text, keyword):
    return encrypt(text, "".join(chr((-(ord(letter) - 65)) % 26 + 65) for letter in keyword))

plaintext = input("Plaintext: ")
keyword = input("Keyword (letters only): ").upper()
if not keyword or not all("A" <= letter <= "Z" for letter in keyword):
    raise ValueError("Enter a keyword containing A-Z letters only")
ciphertext = encrypt(plaintext, keyword)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypt(ciphertext, keyword))
