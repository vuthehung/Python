'''
Project: Random PassWord Generator

PassWord: abcXYZ-69_96
'''

import string
import random

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
PUNCTUATION = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
def random_password(length):
    printTable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    printTable = list(printTable)
    random.shuffle(printTable)
    passWord = random.choices(printTable,k=length)
    passWord = ''.join(passWord)
    return passWord
def get_passWord_length():
    passWord_length = input("How long do you want your password: ")
    return int(passWord_length)
def main():
    passWord_lengt = get_passWord_length()
    pass_word = random_password(passWord_lengt)
    print(pass_word)
if __name__ == '__main__':
    main()