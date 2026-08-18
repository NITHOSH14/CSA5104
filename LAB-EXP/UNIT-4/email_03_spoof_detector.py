# Detect spoofed email addresses by analyzing email headers


def detect_spoofed(from_field, reply_to, received):
    if from_field.lower() != reply_to.lower() and 'example.com' not in from_field.lower():
        return 'Possible spoofing'
    if 'unknown' in received.lower():
        return 'Suspicious routing'
    return 'Looks valid'


if __name__ == '__main__':
    print(detect_spoofed('admin@bank.com', 'support@bank.com', 'mail.example.com'))
    print(detect_spoofed('fake@unknown.net', 'fake@unknown.net', 'unknown'))
