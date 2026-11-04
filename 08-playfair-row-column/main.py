def encrypt(text, key):
    key = key.upper().replace("J", "I")
    letters = ""

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in letters:
            letters += ch

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(letters[i:i+5]))

    text = text.upper().replace("J", "I")
    text = text.replace(" ", "")

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i+1 < len(text):
            b = text[i+1]
        else:
            b = "X"

        if a == b:
            b = "X"
            i += 1
        else:
            i += 2

        r1 = c1 = r2 = c2 = 0

        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += matrix[r1][(c1+1)%5]
            result += matrix[r2][(c2+1)%5]

        elif c1 == c2:
            result += matrix[(r1+1)%5][c1]
            result += matrix[(r2+1)%5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


plain = input("Enter plaintext: ")
key = input("Enter key: ")

print("Cipher text:", encrypt(plain, key))