# Encapsulation/decapsulation process of ESP


def esp_encapsulate(payload: str):
    return {'esp_header': 'SPI+SEQ', 'ciphertext': f'ENC({payload})', 'trailer': 'padding+padlen+nextheader'}


def esp_decapsulate(esp_packet):
    return {'result': f"Decrypt and verify {esp_packet['ciphertext']}", 'payload': 'original message'}


if __name__ == '__main__':
    packet = esp_encapsulate('secret-data')
    print(packet)
    print(esp_decapsulate(packet))
