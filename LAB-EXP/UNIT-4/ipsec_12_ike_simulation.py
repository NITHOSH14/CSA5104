# Simplified IKE protocol simulation


def ike_phase1():
    return {'message': 'ClientHello', 'response': 'ServerHello', 'status': 'secure tunnel ready'}


def ike_phase2():
    return {'message': 'SA negotiation', 'response': 'Key exchange', 'status': 'IPSec session established'}


if __name__ == '__main__':
    print(ike_phase1())
    print(ike_phase2())
