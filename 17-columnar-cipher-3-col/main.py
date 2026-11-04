# Fill the grid across rows, then read each column top to bottom.
text = input("Plaintext: ").upper().replace(" ", "")
columns = 3
text += "X" * (-len(text) % columns)
ciphertext = ""
for column in range(columns):
    ciphertext += text[column::columns]
print("Ciphertext:", ciphertext)
