import random
import string

print('Hello, welcome to Password generator!')
length =int(input('\nEnter the length of password : '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num =string.digits
symbols =string.punctuation

all =lower + upper + num + symbols

a =random.sample(all,length)
password= "".join(a)

print(password)

