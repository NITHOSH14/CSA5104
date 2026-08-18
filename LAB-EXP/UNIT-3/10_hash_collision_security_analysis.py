import hashlib


def hash_messages(messages, algorithm):
    hashes = {}
    for msg in messages:
        digest = hashlib.new(algorithm, msg.encode('utf-8')).hexdigest()
        if digest in hashes:
            print(f'Collision found for {algorithm}: {msg} and {hashes[digest]} produce the same digest: {digest}')
        hashes[digest] = msg
    return hashes


if __name__ == '__main__':
    messages = [
        'hello world',
        'hello world!',
        'Hello World',
        'The quick brown fox jumps over the lazy dog',
        'The quick brown fox jumps over the lazy dog.',
        'security lab',
        'security lab.',
        'student123',
        'student124',
        'message one',
        'message two',
        'another example'
    ]

    print('MD5 Results:')
    md5_map = hash_messages(messages, 'md5')
    print('Unique MD5 digests:', len(md5_map))

    print('\nSHA-256 Results:')
    sha256_map = hash_messages(messages, 'sha256')
    print('Unique SHA-256 digests:', len(sha256_map))

    print('\nSecurity Analysis:')
    print('MD5 and SHA-1 are vulnerable to collision attacks and are not recommended for new security-sensitive applications.')
    print('SHA-256 is stronger because it is more resistant to collisions and is widely used for integrity and digital signatures.')
    print('Collision resistance means that two different inputs should not produce the same hash value.')
