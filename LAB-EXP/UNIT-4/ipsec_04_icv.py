# ICV calculation for AH

import hashlib, hmac


def calculate_icv(data: str, secret: str) -> str:
    return hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()


if __name__ == '__main__':
    data = 'Authentication Header payload'
    secret = 'AH_SECRET_KEY'
    icv = calculate_icv(data, secret)
    print('ICV:', icv)
