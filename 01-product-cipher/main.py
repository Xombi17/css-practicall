text = input("Enter plaintext: ").upper().replace(" ", "")
shift = int(input("Enter shift: ")) % 26
columns = int(input("Enter number of columns: "))
order = input("Enter column order: ").split()
order = [int(x) for x in order]
substituted = ""
for ch in text:
    substituted += chr((ord(ch) - 65 + shift) % 26 + 65)
cipher = ""
for col in order:
    for i in range(col - 1, len(substituted), columns):
        cipher += substituted[i]
print("After substitution:", substituted)
print("Column read order:", order)
print("Product cipher:", cipher)