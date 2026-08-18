# AES 1: AES-128 Encryption and Decryption

from Crypto.Cipher import AES


def pad(data: bytes) -> bytes:
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]


if __name__ == '__main__':
    plain_text = 'AES-128 Demo'.encode()
    key = b'1234567890123456'
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plain_text)
    encrypted = cipher.encrypt(padded)
    decrypted = cipher.decrypt(encrypted)
    print('Plaintext:', plain_text.decode())
    print('Key:', key.decode('latin1'))
    print('Ciphertext (hex):', encrypted.hex())
    print('Decrypted:', unpad(decrypted).decode())
