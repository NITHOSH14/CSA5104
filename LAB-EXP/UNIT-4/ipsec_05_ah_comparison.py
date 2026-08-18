# Compare packet transmission with and without AH

import hashlib, hmac


def without_ah(packet):
    return {'mode': 'without AH', 'integrity': 'not protected'}


def with_ah(packet, key):
    icv = hmac.new(key.encode(), packet.encode(), hashlib.sha256).hexdigest()
    return {'mode': 'with AH', 'integrity': 'protected', 'icv': icv}


if __name__ == '__main__':
    packet = 'Destination=10.0.0.5; payload=login_credentials'
    print(without_ah(packet))
    print(with_ah(packet, 'sharedkey'))
