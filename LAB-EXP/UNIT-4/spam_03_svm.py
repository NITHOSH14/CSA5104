# Support Vector Machine-like simple classifier for spam detection


def svm_like_spam_detector(message):
    tokens = message.lower().split()
    suspicious = {'free', 'click', 'lottery', 'winner', 'urgent', 'claim'}
    score = sum(1 for t in tokens if t in suspicious)
    return score >= 2, score


if __name__ == '__main__':
    msg = 'Urgent message: click now and claim your free reward'
    is_spam, score = svm_like_spam_detector(msg)
    print('Is spam:', is_spam)
    print('Spam score:', score)
