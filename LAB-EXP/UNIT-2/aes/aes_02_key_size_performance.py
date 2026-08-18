# AES 2: Performance Analysis with Different Key Sizes

import time
from Crypto.Cipher import AES


def encrypt_data(key_size: int, message: bytes):
    key = b'A' * key_size
    cipher = AES.new(key, AES.MODE_ECB)
    padded = message + b' ' * ((16 - len(message) % 16) % 16)
    start = time.perf_counter(); cipher.encrypt(padded); enc = time.perf_counter() - start
    start = time.perf_counter(); cipher.decrypt(cipher.encrypt(padded)); dec = time.perf_counter() - start
    return enc, dec


if __name__ == '__main__':
    message = b'This is a sample text for AES performance analysis.' * 200
    print('Key size | encryption time | decryption time')
    for bits in [128, 192, 256]:
        key_len = bits // 8
        enc, dec = encrypt_data(key_len, message)
        print(f'{bits:>7} | {enc*1000:.3f} ms | {dec*1000:.3f} ms')
