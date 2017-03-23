'''QUESTION 4'''

import pickle

from algorithms import move_on

couples_list = pickle.load(open("couple.p", "rb"))

if len(couples_list) >= 1:
    from random import randint
    k = randint(1, len(couples_list))
    move_on(couples_list, k)
