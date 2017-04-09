'''QUESTION 7'''

import pickle

from algorithms import make_couples
from algorithms import give_gifts
from algorithms import move_on

make_couples(True, True)
couples_list = pickle.load(open("couple.p", "rb"))

if len(couples_list) >= 1:
    from random import randint

    t = randint(1, len(couples_list))
    for i in range(t):
        day_name = 'Day ' + str(i + 1)
        give_gifts(True, couples_list, day_name)
        move_on(couples_list, t)
        couples_list = pickle.load(open("couple.p", "rb"))

else:
    print("NO COUPLES FOUND.")