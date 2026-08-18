# RC5 3: Avalanche Effect Analysis

from rc5_01_encryption_decryption import encrypt_block


def bit_diff(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))


if __name__ == '__main__':
    key = 'SecretKey123'
    original = 'Hello World'
    modified = 'Hello Worlx'
    c1 = encrypt_block(original.encode().ljust(8, b' ')[:8], key, 12).hex()
    c2 = encrypt_block(modified.encode().ljust(8, b' ')[:8], key, 12).hex()
    diff_bits = bit_diff(c1, c2)
    avalanche = (diff_bits / (len(c1) * 4)) * 100
    print('Original ciphertext:', c1)
    print('Modified ciphertext:', c2)
    print('Differing bits:', diff_bits)
    print('Avalanche percentage:', round(avalanche, 2), '%')
