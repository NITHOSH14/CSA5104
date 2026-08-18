import hashlib, hmac


def generate_hmac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()


if __name__ == '__main__':
    key = 'secret-key'
    message = 'Verify integrity using HMAC'
    digest = generate_hmac(key, message)
    print('HMAC-SHA256:', digest)
