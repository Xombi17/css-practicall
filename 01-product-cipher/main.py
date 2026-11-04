# First substitute letters, then read the text by columns.
text = input("Plaintext (letters only): ").upper().replace(" ", "")
shift = int(input("Substitution shift: ")) % 26
substituted = ""
for letter in text:
    substituted += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))

columns = 4
padded = substituted + "X" * (-len(substituted) % columns)
ciphertext = ""
for column in range(columns):
    ciphertext += padded[column::columns]

print("After substitution:", substituted)
print("Product cipher:", ciphertext)
