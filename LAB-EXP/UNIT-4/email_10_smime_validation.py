# Certificate validation for S/MIME email communication


def validate_certificate(cert_info):
    required = {'issuer', 'valid_from', 'valid_to', 'public_key'}
    return required.issubset(cert_info.keys())


if __name__ == '__main__':
    cert = {'issuer': 'CA', 'valid_from': '2024-01-01', 'valid_to': '2025-01-01', 'public_key': 'rsa-key'}
    print('Certificate valid:', validate_certificate(cert))
