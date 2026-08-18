# PGP encryption/decryption using simple symmetric-like simulation


def pgp_encrypt(message, key):
    return f'ENC({message})::KEY({key})'


def pgp_decrypt(ciphertext, key):
    return ciphertext.replace(f'::KEY({key})', '').replace('ENC(', '').replace(')', '')


if __name__ == '__main__':
    enc = pgp_encrypt('secret', 'abc123')
    print('Encrypted:', enc)
    print('Decrypted:', pgp_decrypt(enc, 'abc123'))
