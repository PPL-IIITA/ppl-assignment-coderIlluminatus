'''QUESTION 8'''

import pickle
import sys

from algorithms import give_gifts
from algorithms import print_gifts

couples_list = pickle.load(open("couple.p", "rb"))

if len(couples_list) >= 1:
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        choice = 'default'
    give_gifts(couples_list, 'Valentine\'s Day', choice)
    print_gifts(couples_list)

else:
    print("NO COUPLES FOUND.")
