# Blowfish 1: Blowfish Encryption

from Crypto.Cipher import Blowfish


if __name__ == '__main__':
    key = b'SecretKey123'
    message = 'NETWORKSECURITY'.encode()
    padded = message + b' ' * ((8 - len(message) % 8) % 8)
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    print('Plaintext:', message.decode())
    print('Key:', key.decode())
    print('Ciphertext (hex):', ciphertext.hex())
