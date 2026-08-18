# RSA 2: Digital Signature Generation and Verification

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15


def main():
    message = b'Hello from RSA signature demo'
    key = RSA.generate(1024)
    signer = pkcs1_15.new(key)
    digest = SHA256.new(message)
    signature = signer.sign(digest)

    print('Message:', message.decode())
    print('Signature (hex):', signature.hex())

    verifier = pkcs1_15.new(key.publickey())
    try:
        verifier.verify(digest, signature)
        print('Verification: Signature is valid.')
    except ValueError:
        print('Verification: Signature invalid.')

    modified = b'Hello from modified RSA signature demo'
    digest2 = SHA256.new(modified)
    try:
        verifier.verify(digest2, signature)
        print('Verification: Tampered message accepted unexpectedly.')
    except ValueError:
        print('Verification: Modified message rejected successfully.')


if __name__ == '__main__':
    main()
