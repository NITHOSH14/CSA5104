# Extract authentication-related email header fields


def extract_auth_fields(header_text):
    auth_fields = []
    for line in header_text.splitlines():
        if line.lower().startswith(('authentication-results', 'dkim-signature', 'received-spf', 'arc-authentication-results')):
            auth_fields.append(line)
    return auth_fields


if __name__ == '__main__':
    sample = '''Authentication-Results: mx.example.net; dkim=pass
DKIM-Signature: v=1; a=rsa-sha256; d=example.com
Received-SPF: pass (sender SPF authorized)'''
    print(extract_auth_fields(sample))
