# AES 3: Avalanche Effect Analysis

from Crypto.Cipher import AES


def pad(data: bytes) -> bytes:
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def diff_bits(a: str, b: str):
    return sum(x != y for x, y in zip(a, b))


if __name__ == '__main__':
    key = b'1234567890123456'
    original = 'AES avalanche effect'
    changed = 'AES avalanche effecT'
    c1 = AES.new(key, AES.MODE_ECB).encrypt(pad(original.encode()))
    c2 = AES.new(key, AES.MODE_ECB).encrypt(pad(changed.encode()))
    h1 = c1.hex(); h2 = c2.hex()
    changed_bits = diff_bits(h1, h2)
    percent = (changed_bits / len(h1)) * 100
    print('Ciphertext 1:', h1)
    print('Ciphertext 2:', h2)
    print('Changed bits:', changed_bits)
    print('Avalanche percentage:', round(percent, 2), '%')
