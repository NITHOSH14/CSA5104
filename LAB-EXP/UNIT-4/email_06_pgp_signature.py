# Generate and verify digital signatures in a PGP-like model

import hashlib


def sign(message, private_key):
    return hashlib.sha256((private_key + message).encode()).hexdigest()


def verify(message, signature, public_key):
    expected = hashlib.sha256((public_key + message).encode()).hexdigest()
    return signature == expected


if __name__ == '__main__':
    msg = 'Signed contract'
    sig = sign(msg, 'privatekey')
    print('Valid signature:', verify(msg, sig, 'privatekey'))
