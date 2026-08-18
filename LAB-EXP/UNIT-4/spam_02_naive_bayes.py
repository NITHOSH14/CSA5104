# Naive Bayes based spam detection model (educational simulation)


def naive_bayes_score(message, spam_probability=0.5, ham_probability=0.5):
    tokens = set(message.lower().split())
    spam_words = {'free', 'winner', 'win', 'urgent', 'click', 'prize'}
    ham_words = {'meeting', 'project', 'schedule', 'report', 'hello'}

    spam_hits = sum(1 for token in tokens if token in spam_words)
    ham_hits = sum(1 for token in tokens if token in ham_words)

    score = (spam_probability * (spam_hits + 1)) / ((spam_probability * (spam_hits + 1)) + (ham_probability * (ham_hits + 1)))
    return score, spam_hits, ham_hits


if __name__ == '__main__':
    text = 'Urgent click now to win a free prize'
    s, sp, hp = naive_bayes_score(text)
    print('Spam probability:', round(s, 3))
    print('Spam hits:', sp, 'Ham hits:', hp)
    print('Classification: spam' if s >= 0.5 else 'ham')
