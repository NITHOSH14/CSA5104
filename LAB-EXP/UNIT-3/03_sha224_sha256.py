import hashlib


if __name__ == '__main__':
    text = input('Enter a message: ')
    sha224 = hashlib.sha224(text.encode('utf-8')).hexdigest()
    sha256 = hashlib.sha256(text.encode('utf-8')).hexdigest()

    print('\nInput Message:', text)
    print('SHA-224:', sha224)
    print('SHA-224 Length:', len(sha224), 'hex chars = 224 bits')
    print('SHA-256:', sha256)
    print('SHA-256 Length:', len(sha256), 'hex chars = 256 bits')

    if len(sha224) < len(sha256):
        print('Conclusion: SHA-256 output is longer than SHA-224 output.')
    else:
        print('Conclusion: SHA-224 and SHA-256 have different output sizes.')
