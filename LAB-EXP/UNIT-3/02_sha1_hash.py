import hashlib


def sha1_hash(text: str) -> str:
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    message = input('Enter a text message: ')
    digest1 = sha1_hash(message)
    print('Original Message:', message)
    print('SHA-1 Digest 1:', digest1)

    modified = message[:-1] + ('X' if message and message[-1] != 'X' else 'Y')
    digest2 = sha1_hash(modified)
    print('Modified Message:', modified)
    print('SHA-1 Digest 2:', digest2)

    if digest1 == digest2:
        print('Verification: Both digests are identical.')
    else:
        print('Verification: Hash changed after one-character modification.')
