import hashlib


def get_hash(text: str, algorithm: str) -> str:
    algorithms = {
        '1': 'md5',
        '2': 'sha1',
        '3': 'sha224',
        '4': 'sha256',
        '5': 'sha384',
        '6': 'sha512',
    }
    if algorithm not in algorithms:
        raise ValueError('Invalid algorithm choice')
    return hashlib.new(algorithms[algorithm], text.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    print('Hash Algorithm Menu')
    print('1. MD5')
    print('2. SHA-1')
    print('3. SHA-224')
    print('4. SHA-256')
    print('5. SHA-384')
    print('6. SHA-512')

    choice = input('Enter your choice (1-6): ')
    message = input('Enter the message: ')

    try:
        digest = get_hash(message, choice)
        print(f'\nSelected Algorithm: {choice}')
        print('Message:', message)
        print('Digest:', digest)
    except ValueError as e:
        print(e)
