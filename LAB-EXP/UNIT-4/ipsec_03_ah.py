# Authentication Header simulation
# Demonstrates AH processing for integrity and authentication.

import hashlib, hmac


def auth_header_icv(payload: bytes, key: str) -> bytes:
    return hmac.new(key.encode(), payload, hashlib.sha256).digest()


def send_packet_with_ah(payload: bytes, key: str):
    icv = auth_header_icv(payload, key)
    return {'payload': payload, 'AH-ICV': icv.hex()}


def receive_packet_with_ah(packet, key: str):
    expected = auth_header_icv(packet['payload'], key)
    ok = expected.hex() == packet['AH-ICV']
    return {'verified': ok, 'status': 'accepted' if ok else 'rejected'}


if __name__ == '__main__':
    payload = b'IP packet content'
    packet = send_packet_with_ah(payload, 'shared-key')
    print(packet)
    print(receive_packet_with_ah(packet, 'shared-key'))
