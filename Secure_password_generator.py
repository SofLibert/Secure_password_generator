from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
ambiguous_characters = 'il1Lo0O'
chars = []

print('Сколько паролей сгенерировать?')
counter = int(input())

print('Какая длина у пароля?')
length = int(input())

print('Включать ли цифры 0123456789? (Да/Нет)')
answer_1 = input()
if answer_1 == 'Да':
    chars.extend(digits)

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Да/Нет)')
answer_2 = input()
if answer_2 == 'Да':
    chars.extend(uppercase_letters)

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (Да/Нет)')
answer_3 = input()
if answer_3 == 'Да':
    chars.extend(lowercase_letters)

print('Включать ли символы !#$%&*+-=?@^_? (Да/Нет)')
answer_4 = input()
if answer_4 == 'Да':
    chars.extend(punctuation)

print('Исключать ли неоднозначные символы il1Lo0O? (Да/Нет)')
answer_5 = input()
if answer_5 == 'Да':
    for i in range(len(ambiguous_characters)):
        if ambiguous_characters[i] in chars:
            chars.remove(ambiguous_characters[i])

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password

for _ in range(counter):
    print(generate_password(length, chars))