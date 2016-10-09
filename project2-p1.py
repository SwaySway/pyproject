# from random import choice
# from string import ascii_lowercase
# DEFAULT_KEY = "bpzhgocvjdqswkimlutneryaxf"
# ALPHABET = "abcdefghijklmnopqrstuvwxyz"
#
# inv_map = {}
# for i in range(25):
#     inv_map[i] = DEFAULT_KEY[i]
#
# print(inv_map)
#
# print(''.join(choice(ascii_lowercase) for i in range(25)))

import random
chars = 'abcdefghijklmnopqrstuvwxyz'
DEFAULT_KEY = 'bpzhgocvjdqswkimlutneryaxf'
"""Generate an key for our cipher"""

plaintext = "flow"

def keyGen():
    return sorted(chars, key=lambda k: random.random())


def substitionEncrypt():

def substitionDecrypt():

key = dict(zip(chars, DEFAULT_KEY))

"""Encrypt the string and return the ciphertext"""
print(''.join(key[a] for a in plaintext))