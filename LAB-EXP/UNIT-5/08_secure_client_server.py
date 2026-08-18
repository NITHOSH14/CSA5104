import hashlib, hmac


def symmetric_encrypt(key, message):
    digest = hashlib.sha256((key + message).encode()).hexdigest()
    return digest


def secure_send(key, message):
    encrypted = symmetric_encrypt(key, message)
    mac = hmac.new(key.encode(), encrypted.encode(), hashlib.sha256).hexdigest()
    return encrypted, mac


if __name__ == '__main__':
    key = 'shared-secret'
    message = 'Hello from client to server'
    enc, mac = secure_send(key, message)
    print('Encrypted:', enc)
    print('MAC:', mac)
