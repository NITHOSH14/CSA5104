# RC5 1: RC5 Encryption and Decryption

MASK = 0xFFFFFFFF
P = 0xB7E15163
Q = 0x9E3779B9


def rol(value: int, shift: int) -> int:
    shift &= 31
    if shift == 0:
        return value & MASK
    return ((value << shift) | (value >> (32 - shift))) & MASK


def ror(value: int, shift: int) -> int:
    shift &= 31
    if shift == 0:
        return value & MASK
    return ((value >> shift) | (value << (32 - shift))) & MASK


def expand_key(key: str, rounds: int = 12):
    key_bytes = key.encode('utf-8')
    L = [0] * ((len(key_bytes) + 3) // 4)
    for i in range(len(L)):
        word = 0
        for j in range(4):
            idx = i * 4 + j
            if idx < len(key_bytes):
                word |= key_bytes[idx] << (8 * j)
        L[i] = word

    S = [0] * (2 * rounds + 2)
    S[0] = P
    for i in range(1, 2 * rounds + 2):
        S[i] = (S[i - 1] + Q) & MASK

    A = B = i = j = 0
    for _ in range(3 * (2 * rounds + 2)):
        A = S[i] = rol((S[i] + A + B) & MASK, 3)
        B = L[j] = rol((L[j] + A + B) & MASK, (A + B) & 31)
        i = (i + 1) % (2 * rounds + 2)
        j = (j + 1) % len(L)
    return S


def encrypt_block(block: bytes, key: str, rounds: int = 12) -> bytes:
    if len(block) != 8:
        raise ValueError('RC5 operates on 64-bit blocks (8 bytes).')

    S = expand_key(key, rounds)
    a = (int.from_bytes(block[:4], 'little') + S[0]) & MASK
    b = (int.from_bytes(block[4:], 'little') + S[1]) & MASK

    for i in range(1, rounds + 1):
        a = (rol((a ^ b) & MASK, b & 31) + S[2 * i]) & MASK
        b = (rol((b ^ a) & MASK, a & 31) + S[2 * i + 1]) & MASK

    return a.to_bytes(4, 'little') + b.to_bytes(4, 'little')


def decrypt_block(block: bytes, key: str, rounds: int = 12) -> bytes:
    if len(block) != 8:
        raise ValueError('RC5 operates on 64-bit blocks (8 bytes).')

    S = expand_key(key, rounds)
    a = int.from_bytes(block[:4], 'little')
    b = int.from_bytes(block[4:], 'little')

    for i in range(rounds, 0, -1):
        b = (ror((b - S[2 * i + 1]) & MASK, a & 31) ^ a) & MASK
        a = (ror((a - S[2 * i]) & MASK, b & 31) ^ b) & MASK

    a = (a - S[0]) & MASK
    b = (b - S[1]) & MASK
    return a.to_bytes(4, 'little') + b.to_bytes(4, 'little')


if __name__ == '__main__':
    plaintext = 'RC5 Demo'
    key = 'SecretKey123'
    block = plaintext.encode().ljust(8, b' ')[:8]
    encrypted = encrypt_block(block, key)
    decrypted = decrypt_block(encrypted, key)
    print('Plaintext:', plaintext)
    print('Key:', key)
    print('Ciphertext (hex):', encrypted.hex())
    print('Decrypted Plaintext:', decrypted.decode('utf-8').rstrip())
