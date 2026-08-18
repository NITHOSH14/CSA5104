import hashlib


if __name__ == '__main__':
    text = input('Enter a message: ')
    sha384 = hashlib.sha384(text.encode('utf-8')).hexdigest()
    sha512 = hashlib.sha512(text.encode('utf-8')).hexdigest()

    print('\nInput Message:', text)
    print('SHA-384:', sha384)
    print('SHA-384 Length:', len(sha384), 'hex chars = 384 bits')
    print('SHA-512:', sha512)
    print('SHA-512 Length:', len(sha512), 'hex chars = 512 bits')

    print('Comparison: SHA-512 digest is longer than SHA-384 digest.')
