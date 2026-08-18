# DES 5: DES Performance Analysis

import time
from pathlib import Path
from Crypto.Cipher import DES


def encrypt_size(size_bytes):
    key = b'abcdefgh'
    data = b'A' * size_bytes
    pad = data + b' ' * ((8 - len(data) % 8) % 8)
    start = time.perf_counter(); DES.new(key, DES.MODE_ECB).encrypt(pad); enc = time.perf_counter() - start
    start = time.perf_counter(); DES.new(key, DES.MODE_ECB).decrypt(DES.new(key, DES.MODE_ECB).encrypt(pad)); dec = time.perf_counter() - start
    return enc, dec


if __name__ == '__main__':
    print('File size | encrypt time | decrypt time')
    for size in [1024, 10 * 1024, 100 * 1024, 1024 * 1024]:
        enc, dec = encrypt_size(size)
        print(f'{size:>9} | {enc * 1000:.3f} ms | {dec * 1000:.3f} ms')
