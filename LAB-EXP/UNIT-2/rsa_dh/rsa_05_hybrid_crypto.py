# RSA 5: Hybrid Cryptosystem using RSA and AES

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes


def main():
    message = b'Hybrid cryptosystem using RSA and AES'
    key = RSA.generate(1024)
    pub = key.publickey()

    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(pub)
    encrypted_key = cipher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message)

    decrypt_rsa = PKCS1_OAEP.new(key)
    recovered_key = decrypt_rsa.decrypt(encrypted_key)
    cipher_aes2 = AES.new(recovered_key, AES.MODE_EAX, nonce=cipher_aes.nonce)
    recovered = cipher_aes2.decrypt_and_verify(ciphertext, tag)

    print('Original message:', message.decode())
    print('Recovered message:', recovered.decode())
    print('RSA encrypted AES key (hex):', encrypted_key.hex())


if __name__ == '__main__':
    main()
