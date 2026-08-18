# RC5 5: Comparative Analysis of RC5 and AES

import time
from Crypto.Cipher import AES
from rc5_01_encryption_decryption import encrypt_block, decrypt_block


def aes_encrypt(data: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)


def aes_decrypt(data: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)


if __name__ == '__main__':
    plaintext = b'Compare RC5 and AES security and speed'
    key_rc5 = 'SecretKey123'
    key_aes = b'1234567890123456'
    start = time.perf_counter(); enc_rc5 = encrypt_block(plaintext[:8].ljust(8, b' '), key_rc5, 12); rc5_enc = time.perf_counter() - start
    start = time.perf_counter(); dec_rc5 = decrypt_block(enc_rc5, key_rc5, 12); rc5_dec = time.perf_counter() - start
    pad = plaintext + b' ' * ((16 - len(plaintext) % 16) % 16)
    start = time.perf_counter(); aes_cipher = aes_encrypt(pad, key_aes); aes_enc = time.perf_counter() - start
    start = time.perf_counter(); aes_plain = aes_decrypt(aes_cipher, key_aes); aes_dec = time.perf_counter() - start

    print('RC5 encrypt time:', rc5_enc)
    print('RC5 decrypt time:', rc5_dec)
    print('AES encrypt time:', aes_enc)
    print('AES decrypt time:', aes_dec)
    print('RC5 block size: 64 bits')
    print('AES block size: 128 bits')
    print('RC5 rounds: variable')
    print('AES rounds: 10/12/14 depending on key size')
