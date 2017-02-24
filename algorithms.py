'''ALL ALGORITHMIC OPERATIONS'''

from random import randint
from random import choice
import csv
import logging

def create(filename, datalist):
    '''CREATES csv ROWS FROM GIVEN DATA SET'''
    newfile = open(filename, 'w')
    writer = csv.writer(newfile, delimiter=',')

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
                 randint(1, 100),\
                 choice(boys_nature))
                  for i in range(n_boys)])

    girls_list = ([('Girl '+str(i + 1),\
                 randint(1, 100),\
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
    gifts_list = []

    for i in range(n_gifts):
        current_gift_type = choice(gift_type)
        if current_gift_type == 'Essential':
            gifts_list[i] = ('Gift '+str(i + 1),\
                            randint(1, 100),\
                            randint(1, 100),\
                            choice(gift_type))
        elif current_gift_type == 'Luxury':
            gifts_list[i] = ('Gift '+str(i + 1),\
                            randint(1, 100),\
                            randint(1, 100),\
                            choice(gift_type),\
                            randint(1, 5),\
                            randint(1, 5))
        elif current_gift_type == 'Utility':
            gifts_list[i] = ('Gift '+str(i + 1),\
                            randint(1, 100),\
                            randint(1, 100),\
                            choice(gift_type),\
                            randint(1, 10),\
                            randint(1, 10))

    create('gifts.csv', gifts_list)


#SPECIFYING FORMAT OF EVENT LOG
logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
					datefmt='%d/%m/%Y %I:%M:%S %p',\
					level=logging.DEBUG,\
                    filename='eventlog.txt',\
                    filemode='w')

def make_couples():
    '''FORMS COUPLES BASED ON BUDGET AND MAINTENANCE CRITERIA'''
    from boys.boy_uninherited import Boy
    from girls.girl_uninherited import Girl

    with open('boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        boy_pool = [Boy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))\
                     for row in reader]
        csvfile.close()

    with open('girls.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        girl_pool = [Girl(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))\
                      for row in reader]
        csvfile.close()

    logging.info('\nFINDING SUITABLE MATCH FOR GIRLS\n')
    for girl in girl_pool:
        for boy in boy_pool:
            logging.info('COURTING   :\t' + girl.name + ' is checking out ' + boy.name)
            if boy.check_elligibility(girl) and girl.check_elligibility(boy):
                boy.status, girl.status = 'Committed', 'Committed'
                boy.partner, girl.partner = girl.name, boy.name
                logging.info('MATCHED    :\t' + girl.name + ' is committed with ' + boy.name + '\n')
                break

    print('COUPLES FORMED\n')
    for girl in girl_pool:
        if girl.status == 'Committed':
            print(girl.name + '\t  AND\t' + girl.partner)
