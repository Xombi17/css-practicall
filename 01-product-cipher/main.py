# Substitute letters, then read columns in the user-specified order (1-based).
text = input("Plaintext (letters only): ").upper().replace(" ", "")
shift = int(input("Substitution shift: ")) % 26
columns = int(input("Number of transposition columns: "))
if not text.isascii() or not text.isalpha():
    raise ValueError("Use A-Z letters only")
if columns < 1:
    raise ValueError("Columns must be at least 1")
order = [int(value) for value in input(f"Column read order (1 to {columns}, e.g. {' '.join(map(str, range(1, columns + 1)))}): ").split()]
if sorted(order) != list(range(1, columns + 1)):
    raise ValueError(f"Enter each column number from 1 to {columns} exactly once")

substituted = ""
for letter in text:
    if "A" <= letter <= "Z":
        substituted += chr((ord(letter) - 65 + shift) % 26 + 65)
ciphertext = ""
for column in order:
    ciphertext += substituted[column - 1::columns]

print("After substitution:", substituted)
print("Column read order:", order)
print("Product cipher:", ciphertext)
