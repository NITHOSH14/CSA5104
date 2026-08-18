signatures = ['DROP_TABLE', 'SQLI', 'MALFORMED']


def ips_block(packet):
    for sig in signatures:
        if sig in packet:
            return 'BLOCKED'
    return 'ALLOWED'


if __name__ == '__main__':
    print(ips_block('SQLI payload detected'))
