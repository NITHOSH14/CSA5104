from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()


def create_dual_signature(order_info, payment_info, private_key):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(order_info + payment_info)
    digest_value = digest.finalize()
    return private_key.sign(digest_value, padding.PKCS1v15(), hashes.SHA256())


if __name__ == '__main__':
    private_key, public_key = generate_keys()
    signature = create_dual_signature(b'order', b'payment', private_key)
    print('Dual signature created:', len(signature), 'bytes')
