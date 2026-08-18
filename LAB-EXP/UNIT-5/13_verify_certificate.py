from cryptography import x509
import datetime


def verify_certificate(cert_path):
    with open(cert_path, 'rb') as f:
        cert = x509.load_pem_x509_certificate(f.read())
    now = datetime.datetime.utcnow()
    print('Issuer:', cert.issuer.rfc4514_string())
    print('Subject:', cert.subject.rfc4514_string())
    print('Not Before:', cert.not_valid_before)
    print('Not After :', cert.not_valid_after)
    print('Valid now:', cert.not_valid_before <= now <= cert.not_valid_after)
    print('Public key type:', type(cert.public_key()).__name__)


if __name__ == '__main__':
    verify_certificate('server.crt')
