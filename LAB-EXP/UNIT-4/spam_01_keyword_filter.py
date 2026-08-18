# Spam detection using a keyword-based filter


def spam_keyword_filter(message):
    keywords = ['free', 'winner', 'lottery', 'click now', 'urgent', 'claim prize', 'limited time']
    msg = message.lower()
    hits = [word for word in keywords if word in msg]
    return {
        'spam_score': len(hits),
        'matched_keywords': hits,
        'is_spam': len(hits) >= 2,
    }


if __name__ == '__main__':
    sample = 'Congratulations! You are a lucky winner. Click now to claim your prize.'
    result = spam_keyword_filter(sample)
    print(result)
