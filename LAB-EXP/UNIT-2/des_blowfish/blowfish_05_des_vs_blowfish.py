# Blowfish 5: DES vs Blowfish Performance Comparison

import time
from Crypto.Cipher import DES, Blowfish


def bench(algorithm, key, data):
    start = time.perf_counter(); algorithm.new(key, algorithm.MODE_ECB).encrypt(data); enc = time.perf_counter() - start
    start = time.perf_counter(); algorithm.new(key, algorithm.MODE_ECB).decrypt(algorithm.new(key, algorithm.MODE_ECB).encrypt(data)); dec = time.perf_counter() - start
    return enc, dec


if __name__ == '__main__':
    data = b'A' * 10000
    des_key = b'abcdefgh'
    bf_key = b'SecretKey123'
    des_enc, des_dec = bench(DES, des_key, data)
    bf_enc, bf_dec = bench(Blowfish, bf_key, data)
    print('Algorithm | encryption time | decryption time')
    print(f'DES       | {des_enc*1000:.3f} ms | {des_dec*1000:.3f} ms')
    print(f'Blowfish  | {bf_enc*1000:.3f} ms | {bf_dec*1000:.3f} ms')
