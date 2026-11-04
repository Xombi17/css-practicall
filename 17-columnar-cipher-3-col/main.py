def encrypt(text, columns):
    text = text.upper().replace(" ", "")
    text += "X" * (-len(text) % columns)
    ciphertext = ""
    for column in range(columns):
        ciphertext += text[column::columns]
    return ciphertext

plaintext = input("Plaintext: ")
print("Ciphertext:", encrypt(plaintext, 3))
