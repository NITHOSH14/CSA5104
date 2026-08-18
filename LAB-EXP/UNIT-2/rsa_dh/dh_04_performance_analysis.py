# Diffie-Hellman 4: Performance Analysis using Different Prime Sizes

import time


def measure(p_bits):
    p = 2 ** p_bits - 1
    g = 2
    a = 7
    b = 11
    start = time.perf_counter()
    pa = pow(g, a, p)
    pb = pow(g, b, p)
    shared_a = pow(pb, a, p)
    shared_b = pow(pa, b, p)
    elapsed = time.perf_counter() - start
    print(f'{p_bits:>4} bits | time: {elapsed:.6f}s | keys match: {shared_a == shared_b}')


if __name__ == '__main__':
    for bits in [128, 256, 512, 1024]:
        measure(bits)
