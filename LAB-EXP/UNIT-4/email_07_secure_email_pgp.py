# Secure email transmission using PGP model


def secure_email(message, public_key):
    encrypted = f'PGP_ENC({message})'
    return {'public_key': public_key, 'encrypted': encrypted}


def receive_secure_email(mail, private_key):
    return f'DECRYPTED with {private_key}: {mail["encrypted"]}'


if __name__ == '__main__':
    mail = secure_email('Send securely', 'alice-public-key')
    print(mail)
    print(receive_secure_email(mail, 'alice-private-key'))
