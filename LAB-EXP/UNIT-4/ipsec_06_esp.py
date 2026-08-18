# ESP protocol simulation
# Encrypts payload and authenticates it.

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


def esp_encrypt(plaintext: bytes, key: bytes):
    nonce = os.urandom(12)
    cipher = AESGCM(key)
    ciphertext = cipher.encrypt(nonce, plaintext, None)
    return nonce, ciphertext


def esp_decrypt(nonce: bytes, ciphertext: bytes, key: bytes):
    cipher = AESGCM(key)
    return cipher.decrypt(nonce, ciphertext, None)


if __name__ == '__main__':
    key = AESGCM.generate_key(bit_length=128)
    raw = b'Confidential IPSec packet'
    nonce, enc = esp_encrypt(raw, key)
    dec = esp_decrypt(nonce, enc, key)
    print('Ciphertext length:', len(enc))
    print('Decrypted:', dec.decode())
