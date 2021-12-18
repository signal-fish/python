import random

print("Welcome to your password generator:")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*0123456789'

length = int(input("Input your password length: "))
passwords = ''

for c in range(length):
    passwords += random.choice(chars)
print(passwords)
