def encrypt(text, columns, order):
    text = text.upper().replace(" ", "")
    text += "X" * (-len(text) % columns)
    ciphertext = ""
    for column in order:
        ciphertext += text[column - 1::columns]
    return ciphertext

plaintext = input("Plaintext: ")
columns = int(input("Number of columns [3 for this practical]: ") or 3)
if columns < 1:
    raise ValueError("Enter at least one column")
order_text = input(f"Column read order, e.g. {' '.join(map(str, range(columns, 0, -1)))} (Enter for normal): ")
order = list(map(int, order_text.split())) if order_text else list(range(1, columns + 1))
if sorted(order) != list(range(1, columns + 1)):
    raise ValueError("Order must list every column number once")
print("Ciphertext:", encrypt(plaintext, columns, order))
