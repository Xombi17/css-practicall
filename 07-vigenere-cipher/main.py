# Repeat the keyword and add its letter values to the plaintext values.
text = input("Plaintext: ").upper()
key = input("Keyword (letters only): ").upper()
if not key or not all("A" <= letter <= "Z" for letter in key):
    raise ValueError("Enter a keyword containing A-Z letters only")
letters = [letter for letter in text if "A" <= letter <= "Z"]
if not letters:
    raise ValueError("Enter at least one letter")
repeated_key = (key * (len(letters) // len(key) + 1))[:len(letters)]

ciphertext = ""
key_position = 0
for letter in text:
    if "A" <= letter <= "Z":
        value = ord(letter) - 65 + ord(repeated_key[key_position]) - 65
        ciphertext += chr(value % 26 + 65)
        key_position += 1
    else:
        ciphertext += letter
print("Ciphertext:", ciphertext)
