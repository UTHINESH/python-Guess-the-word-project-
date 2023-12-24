import random

print("Welcome to random password generator !")
print()
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;:,.<>?'

password_length = int(input("Enter the length of your password: "))

num_passwords = int(input("Enter how many passwords you want: "))

for _ in range(num_passwords):
    password = ''
    for _ in range(password_length):
        password = password + random.choice(characters)

    print("Generated Password:", password)
