# Secure email analyzer combining spam and phishing checks


def secure_email_analyzer(message):
    spam_keywords = ['free', 'winner', 'urgent', 'limited time', 'click now']
    phishing_keywords = ['verify account', 'suspicious login', 'bank account', 'action required']

    text = message.lower()
    spam_hits = [k for k in spam_keywords if k in text]
    phishing_hits = [k for k in phishing_keywords if k in text]

    result = {
        'spam_hits': spam_hits,
        'phishing_hits': phishing_hits,
        'is_spam': bool(spam_hits),
        'is_phishing': bool(phishing_hits),
        'status': 'BLOCKED' if spam_hits or phishing_hits else 'SAFE',
    }
    return result


if __name__ == '__main__':
    sample = 'Urgent action required: verify your account immediately to avoid suspension.'
    print(secure_email_analyzer(sample))
