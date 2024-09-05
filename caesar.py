alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(text, key):
    text = text.upper()
    text = text.replace(" ", "")
    result = ""
    for char in text:
        for letter in alphabet:
            if letter == char:
                i = alphabet.index(letter)
                i += key
                if i >= 26:
                    i -= 26
                result += alphabet[i]
    return result

def decrypt(text, key):
    text = text.upper()
    text = text.replace(" ", "")
    result = ""
    for char in text:
        for letter in alphabet:
            if letter == char:
                i = alphabet.index(letter)
                i -= key
                if i >= 26:
                    i -= 26
                result += alphabet[i]
    return result
if __name__ == '__main__':
    text = "Test for encryption"
    encrypted_text = encrypt(text, 25)
    print(encrypted_text)
    print(decrypt(encrypted_text, 25))