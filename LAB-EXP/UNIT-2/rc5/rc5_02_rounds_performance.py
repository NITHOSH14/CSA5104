# RC5 2: Performance Analysis with Different Number of Rounds

import time
from rc5_01_encryption_decryption import encrypt_block, decrypt_block


def benchmark(rounds):
    key = 'SecretKey123'
    block = b'RC5Demo!'
    start = time.perf_counter()
    enc = encrypt_block(block, key, rounds)
    enc_time = time.perf_counter() - start
    start = time.perf_counter()
    dec = decrypt_block(enc, key, rounds)
    dec_time = time.perf_counter() - start
    print(f'{rounds:>2} rounds | encryption: {enc_time*1000:.3f} ms | decryption: {dec_time*1000:.3f} ms')


if __name__ == '__main__':
    for r in [8, 12, 16, 20]:
        benchmark(r)
