# Simplified PGP model demonstration


def pgp_send(public_key, message):
    return {'encrypted': f'ENC({message}) using {public_key}', 'public_key': public_key}


def pgp_receive(private_key, packet):
    return f'DEC({packet["encrypted"]}) using {private_key}'


if __name__ == '__main__':
    packet = pgp_send('AlicePublicKey', 'Confidential message')
    print(packet)
    print(pgp_receive('AlicePrivateKey', packet))
