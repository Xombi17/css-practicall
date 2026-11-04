text = input("Enter plaintext: ").upper().replace(" ", "")
key = input("Enter key: ").upper().replace(" ", "")

if len(text) != len(key):
    print("Key length must be equal to text length")
else:
    cipher = ""

    for i in range(len(text)):
        p = ord(text[i]) - 65
        k = ord(key[i]) - 65
        c = (p + k) % 26
        cipher += chr(c + 65)

    print("Ciphertext:", cipher)
    