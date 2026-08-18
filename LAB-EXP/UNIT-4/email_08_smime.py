# S/MIME-style email encryption and signing simulation


def smime_encrypt(message, certificate):
    return {'certificate': certificate, 'ciphertext': f'ENC({message})'}


def smime_sign(message, private_key):
    return {'signature': f'SIGN({message}) using {private_key}', 'message': message}


if __name__ == '__main__':
    env = smime_encrypt('Important email', 'certificate_x509')
    signed = smime_sign('Important email', 'private_key_x509')
    print(env)
    print(signed)
