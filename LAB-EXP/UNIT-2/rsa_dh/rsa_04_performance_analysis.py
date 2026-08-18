# RSA 4: Performance Analysis of RSA using different key sizes

import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def measure(key_size):
    message = b'RSA performance analysis message'
    start = time.perf_counter()
    key = RSA.generate(key_size)
    gen_time = time.perf_counter() - start

    pub = key.publickey()
    cipher = PKCS1_OAEP.new(pub)
    start = time.perf_counter()
    ciphertext = cipher.encrypt(message)
    enc_time = time.perf_counter() - start

    dec = PKCS1_OAEP.new(key)
    start = time.perf_counter()
    dec.decrypt(ciphertext)
    dec_time = time.perf_counter() - start

    print(f'{key_size:>4} bits | keygen: {gen_time:.6f}s | encrypt: {enc_time:.6f}s | decrypt: {dec_time:.6f}s')


if __name__ == '__main__':
    print('KeySize | keygen(s) | encrypt(s) | decrypt(s)')
    for bits in [512, 1024, 2048]:
        measure(bits)
