# Combined AH + ESP simulation for confidentiality + integrity + authentication

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os, hashlib, hmac


def ah_digest(data, key):
    return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()


def esp_encrypt(payload, key):
    nonce = os.urandom(12)
    cipher = AESGCM(key)
    return nonce, cipher.encrypt(nonce, payload.encode(), None)


def combine_ah_esp(payload, key):
    ah = ah_digest(payload, key)
    nonce, encrypted = esp_encrypt(payload, key.encode())
    return {'payload': payload, 'AH': ah, 'ESP_nonce': nonce.hex(), 'ESP_ciphertext': encrypted.hex()}


if __name__ == '__main__':
    packet = combine_ah_esp('Secure email or payload', 'verysecurekey')
    print(packet)
