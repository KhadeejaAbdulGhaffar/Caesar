key = int(input("Enter key: "))

plaintext = input("Enter plaintext: ")
ciphertext = ""

for char in plaintext:
    if char.isalpha():
        if char.isupper():
            ciphertext += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) - 97 + key) % 26 + 97)
    else:
        ciphertext += char

print(f"Ciphertext : {ciphertext}")
