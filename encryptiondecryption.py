# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16lrfgnK0VEPmkuoe8B5xRFpFQRJtYntX
"""

def encrypt(string, shift):

    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher


def decrypt(string, shift):

    word = ''
    for char in string:
        if char == ' ':
            word = word + char
        elif char.isupper():
            word = word + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            word = word + chr((ord(char) - shift - 97) % 26 + 97)

    return word


c = input("if you want to encrypt press e,if u want to decrypt press d s")
if c == 'e':
    text = input("enter string: ")
    s = int(input("enter shift number: "))
    print("original string: ", text)
    print("after encryption: ", encrypt(text, s))
elif c == 'd':
    text = input("enter encrypted text: ")
    s = int(input("enter shift number: "))
    print("encrypted text: ", text)
    print("after decryption: ", decrypt(text, s))

pip install xlsxwriter