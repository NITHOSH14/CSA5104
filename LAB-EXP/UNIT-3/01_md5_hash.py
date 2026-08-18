import hashlib


def md5_hash(message: str) -> str:
    return hashlib.md5(message.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    text = input('Enter a message: ')
    digest = md5_hash(text)
    print('\nInput Message:', text)
    print('Message Length:', len(text))
    print('MD5 Digest (128-bit):', digest)
    print('Digest Length (hex chars):', len(digest))
