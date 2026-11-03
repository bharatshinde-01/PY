text = input("Enter plain text: ")

shift = 3
cipher = ""

for ch in text:
    if ch.isupper():
        cipher += chr((ord(ch) - 65 + shift) % 26 + 65)

    elif ch.islower():
        cipher += chr((ord(ch) - 97 + shift) % 26 + 97)

    else:
        cipher += ch

print("Plain Text:", text)
print("Cipher Text:", cipher)