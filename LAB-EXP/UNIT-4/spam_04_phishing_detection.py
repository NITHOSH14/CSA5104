# Phishing email detection simulation


def detect_phishing(email_text):
    phishing_markers = ['verify account', 'urgent action required', 'bank account', 'login now', 'suspicious activity']
    text = email_text.lower()
    markers_found = [marker for marker in phishing_markers if marker in text]
    return {
        'is_phishing': bool(markers_found),
        'markers_found': markers_found,
        'risk_level': 'high' if len(markers_found) >= 2 else 'medium' if markers_found else 'low',
    }


if __name__ == '__main__':
    sample = 'Urgent action required: verify your bank account immediately.'
    print(detect_phishing(sample))
