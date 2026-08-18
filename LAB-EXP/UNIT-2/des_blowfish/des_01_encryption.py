# DES 1: DES Encryption

from Crypto.Cipher import DES


if __name__ == '__main__':
    key = b'12345678'
    message = 'COMPUTER'.encode()
    padded = message + b' ' * ((8 - len(message) % 8) % 8)
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(padded)
    print('Plaintext:', message.decode())
    print('Key:', key)
    print('Ciphertext (hex):', ciphertext.hex())
