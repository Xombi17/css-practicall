def encrypt(text, columns, order):
    text = text.upper().replace(" ", "")


    cipher = ""

    for col in order:
        cipher += text[col-1::columns]

    return cipher


plaintext = input("Enter plaintext: ")
columns = int(input("Enter number of columns: ") or 4)

order = input("Enter column order: ")

if order:
    order = list(map(int, order.split()))
else:
    order = list(range(1, columns+1))

print("Ciphertext:", encrypt(plaintext, columns, order))