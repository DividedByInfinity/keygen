import secrets
from string import ascii_letters, digits
from xml.etree.ElementTree import tostring

key = ['n', 'a', 'a', 'n', '', 'n', 'n', 'a', 'a', '', 'a', 'a', 'n', 'n', '', 'n', 'n', 'n', 'n']

times = int(input("How many keys would you like to generate: "))

for x in range(times):

    alpha = []
    letter = 0

    digitz = []
    num = 0

    generated_key = ''

    for letters in range(7):
        alpha.append(secrets.choice(ascii_letters))

    for numbers in range(11):
        digitz.append(secrets.choice(digits))

    for i, val in enumerate(key):
        if key[i] == 'a':
            generated_key += alpha[letter]
            letter += 1
        elif key[i] == 'n':
            generated_key += digitz[num]
            num += 1
        else:
            generated_key += '-'
    
    print(generated_key)

