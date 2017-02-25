'''QUESTION 2'''

from test_utility import random_generator_people
from test_utility import random_generator_gifts
from algorithms import make_couples
from algorithms import give_gifts
from algorithms import print_gifts
from algorithms import print_happy_couples
from algorithms import print_compatible_couples

random_generator_people()
random_generator_gifts()

couples_list = make_couples(False)

give_gifts(False, couples_list)

print_gifts(couples_list)

from random import randint
k = randint(1, len(couples_list))
print_happy_couples(couples_list, int(k))
print_compatible_couples(couples_list, int(k))