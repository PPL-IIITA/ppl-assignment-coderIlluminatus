'''TEST UTILITY TO RANDOMLY GENERATE csv FILES'''

from random import randint
from random import choice
import csv

def create(filename, datalist):
    '''CREATES csv ROWS FROM GIVEN DATA SET'''
    newfile = open(filename, 'w')
    writer = csv.writer(newfile, delimiter=',')

    for i in datalist:
        writer.writerow(i)

def random_generator_people():
    '''GENERATES RANDOM LIST OF BOYS AND GIRLS'''
    n_boys = randint(11, 20)
    n_girls = randint(10, (n_boys-1))

    boys_nature = ['Miser', 'Generous', 'Geek']
    girls_nature = ['Choosy', 'Normal', 'Desparate']
    girls_criteria = ['Attractive', 'Rich', 'Intelligent']

    boys_list = ([('Boy '+str(i + 1),\
                 randint(1, 100),\
                 randint(1, 100),\
                 randint(1, 100),\
                 randint(1, 100),\
                 choice(boys_nature))
                  for i in range(n_boys)])

    girls_list = ([('Girl '+str(i + 1),\
                 randint(1, 100),\
                 randint(1, 100),\
                 randint(1, 100),\
                 choice(girls_nature),\
                 choice(girls_criteria))
                   for i in range(n_girls)])

    create('boys.csv', boys_list)
    create('girls.csv', girls_list)

def random_generator_gifts():
    '''GENERATES RANDOM LIST OF BOYS AND GIRLS'''
    n_gifts = randint(100, 200)

    gift_type = ['Essential', 'Luxury', 'Utility']
    gifts_list = []

    for i in range(n_gifts):
        current_gift_type = choice(gift_type)
        if current_gift_type == 'Essential':
            gifts_list.append(('Gift '+str(i + 1),\
                            randint(1, 100),\
                            randint(1, 100),\
                            current_gift_type))
        elif current_gift_type == 'Luxury':
            gifts_list.append(('Gift '+str(i + 1),\
                            randint(1, 100),\
                            randint(1, 100),\
                            current_gift_type,\
                            randint(1, 5),\
                            randint(1, 5)))
        elif current_gift_type == 'Utility':
            gifts_list.append(('Gift '+str(i + 1),\
                            randint(1, 100),\
                            randint(1, 100),\
                            current_gift_type,\
                            randint(1, 10),\
                            randint(1, 10)))

    create('gifts.csv', gifts_list)

if __name__ == "__main__":
    random_generator_people()
    random_generator_gifts()