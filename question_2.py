'''QUESTION 2'''

import pickle

from algorithms import give_gifts
from algorithms import print_gifts
from algorithms import print_happy_couples
from algorithms import print_compatible_couples

couples_list = pickle.load(open("couple.p", "rb"))

if len(couples_list) >= 1:
    give_gifts(False, couples_list)

    print_gifts(couples_list)

    from random import randint
    k = randint(1, len(couples_list))
    print_happy_couples(couples_list, int(k))
    print_compatible_couples(couples_list, int(k))

else:
    print("NO COUPLES FOUND.")