'''ALL ALGORITHMIC OPERATIONS'''

from random import randint
from random import choice
import csv

def create(filename, datalist):
    '''CREATES csv ROWS FROM GIVEN DATA SET'''
    newfile = open(filename, 'w')
    writer = csv.writer(newfile, delimeter=',')

    for i in datalist:
        writer.writerow(i)

def random_generator_people():
    '''GENERATES RANDOM LIST OF BOYS AND GIRLS'''
    n_boys = randint(10, 20)
    n_girls = randint(10, n_boys-1)

    boys_nature = ['Miser', 'Generous', 'Geek']
    girls_nature = ['Choosy', 'Normal', 'Desparate']

    boys_list = ([('Boy '+str(i + 1),\
                 randint(1, 100),\
                 randint(1, 100),\
                 randint(1, 100),\
                 randint(1, 100),\
                 choice(boys_nature))
                  for i in range(n_boys)])

    girls_list = ([('Boy '+str(i + 1),\
                 randint(1, 100),\
                 randint(1, 100),\
                 randint(1, 100),\
                 choice(girls_nature))
                   for i in range(n_girls)])

    create('boys.csv', boys_list)
    create('girls.csv', girls_list)

def random_generator_gifts():
    '''GENERATES RANDOM LIST OF BOYS AND GIRLS'''
    n_gifts = randint(100, 200)

    gift_type = ['Essential', 'Luxury', 'Utility']

    gifts_list = ([('Boy '+str(i + 1),\
                 randint(1, 100),\
                 randint(1, 100),\
                 choice(gift_type))
                   for i in range(n_gifts)])

    create('gifts.csv', gifts_list)
