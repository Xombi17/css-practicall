# Substitute letters, then read the padded text by the chosen columns.
text = input("Plaintext (letters only): ").upper().replace(" ", "")
shift = int(input("Substitution shift: ")) % 26
columns = int(input("Number of transposition columns: "))
if not text.isascii() or not text.isalpha():
    raise ValueError("Use A-Z letters only")
if columns < 1:
    raise ValueError("Columns must be at least 1")

substituted = ""
for letter in text:
    if "A" <= letter <= "Z":
        substituted += chr((ord(letter) - 65 + shift) % 26 + 65)
padded = substituted + "X" * (-len(substituted) % columns)
ciphertext = ""
for column in range(columns):
    ciphertext += padded[column::columns]

print("After substitution:", substituted)
print("Padded text:", padded)
print("Product cipher:", ciphertext)
