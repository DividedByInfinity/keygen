from string import digits
from key_generator.key_generator import generate
import secrets

num = int(input('How many keys would you like to generate: '))

for x in range(num):
    custom_key = generate(
        4, 
        '-', 
        4, 
        4, 
        type_of_value='char', 
        capital='mix', 
        extras=list(digits), 
        seed=secrets.randbelow(9999999)
        ).get_key()
    print(custom_key)
