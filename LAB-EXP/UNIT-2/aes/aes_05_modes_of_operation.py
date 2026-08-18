# AES 5: Comparative Analysis of AES Modes of Operation

import time
from Crypto.Cipher import AES


def pad(data: bytes) -> bytes:
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def run_mode(mode_name, mode, data, key):
    cipher = AES.new(key, mode)
    start = time.perf_counter(); ciphertext = cipher.encrypt(pad(data)); enc = time.perf_counter() - start
    start = time.perf_counter(); cipher2 = AES.new(key, mode); cipher2.decrypt(ciphertext); dec = time.perf_counter() - start
    print(f'{mode_name:<6} | encryption: {enc*1000:.3f} ms | decryption: {dec*1000:.3f} ms')


if __name__ == '__main__':
    data = b'Comparing AES modes of operation for educational lab work.' * 100
    key = b'1234567890123456'
    print('Mode   | encryption | decryption')
    run_mode('ECB', AES.MODE_ECB, data, key)
    run_mode('CBC', AES.MODE_CBC, data, key)
    run_mode('CFB', AES.MODE_CFB, data, key)
    run_mode('OFB', AES.MODE_OFB, data, key)
    run_mode('CTR', AES.MODE_CTR, data, key)
