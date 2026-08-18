import hashlib


def sha256_digest(data):
    return hashlib.sha256(data.encode()).hexdigest()


if __name__ == '__main__':
    message = 'This message must be verified'
    digest = sha256_digest(message)
    print('Message:', message)
    print('SHA-256:', digest)
