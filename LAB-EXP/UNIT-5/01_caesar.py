def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(ch)
    return ''.join(result)


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


if __name__ == '__main__':
    message = 'HELLO WORLD'
    shift = 3
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    print('Original :', message)
    print('Encrypted:', encrypted)
    print('Decrypted:', decrypted)
