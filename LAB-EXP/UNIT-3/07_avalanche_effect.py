import hashlib


messages = ['Hello World', 'Hello world']

for msg in messages:
    print(f'\nMessage: {msg}')
    print('MD5   :', hashlib.md5(msg.encode()).hexdigest())
    print('SHA-1 :', hashlib.sha1(msg.encode()).hexdigest())
    print('SHA-256:', hashlib.sha256(msg.encode()).hexdigest())

print('\nAnalysis: A single-character change causes a completely different digest.')
print('This is known as the avalanche effect, which is a desired property of secure hash functions.')
