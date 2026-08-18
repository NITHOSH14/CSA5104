# Analyze email header and identify sender, receiver, route, and timestamps


def parse_email_header(header_text):
    header = {}
    for line in header_text.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            header[key.strip()] = value.strip()
    return header


if __name__ == '__main__':
    sample = '''From: alice@example.com
To: bob@example.com
Subject: Project Update
Date: Tue, 10 Sep 2024 09:15:00 +0000
Received: from mail.example.com by mx.example.net'''
    h = parse_email_header(sample)
    print(h)
    print('Sender:', h.get('From'))
    print('Receiver:', h.get('To'))
    print('Date:', h.get('Date'))
