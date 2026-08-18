def generate_key(message, key):
    key = key.upper()
    key_stream = []
    j = 0
    for ch in message:
        if ch.isalpha():
            key_stream.append(key[j % len(key)])
            j += 1
    return key_stream


def vigenere_encrypt(message, key):
    result = []
    key_stream = generate_key(message, key)
    j = 0
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key_stream[j]) - ord('A')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            j += 1
        else:
            result.append(ch)
    return ''.join(result)


def vigenere_decrypt(ciphertext, key):
    result = []
    key_stream = generate_key(ciphertext, key)
    j = 0
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key_stream[j]) - ord('A')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            j += 1
        else:
            result.append(ch)
    return ''.join(result)


if __name__ == '__main__':
    text = 'ATTACKATDAWN'
    key = 'MONKEY'
    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print('Original :', text)
    print('Encrypted:', encrypted)
    print('Decrypted:', decrypted)
