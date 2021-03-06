'''QUESTION 6'''

import pickle

from algorithms import make_couples
from algorithms import give_gifts
from algorithms import move_on

make_couples(True)
couples_list = pickle.load(open("couple.p", "rb"))

if len(couples_list) >= 1:
    from random import randint

    t = randint(1, len(couples_list))
    for i in range(t):
        day_name = 'Day ' + str(i + 1)
        give_gifts(couples_list, day_name, 'default')
        move_on(couples_list, t)
        couples_list = pickle.load(open("couple.p", "rb"))

else:
    print("NO COUPLES FOUND.")