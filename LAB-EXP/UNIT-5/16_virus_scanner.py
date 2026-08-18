def scan_for_signature(filename):
    signatures = ['MALWARE', 'VIRUS', 'EXE']
    with open(filename, 'rb') as f:
        data = f.read().decode('latin1', 'ignore')
    matches = [sig for sig in signatures if sig in data.upper()]
    return matches


if __name__ == '__main__':
    print(scan_for_signature('sample.bin'))
