'''ALL ALGORITHMIC OPERATIONS'''

import csv
import logging

def make_couples(is_inherited):
    '''FORMS COUPLES BASED ON BUDGET AND MAINTENANCE CRITERIA'''
    if is_inherited:
        from boys.boy import Boy
        from girls.girl import Girl
    else:
        from boys.boy_uninherited import Boy
        from girls.girl_uninherited import Girl
    from couple import Couple

    with open('boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        boy_pool = [Boy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))\
                     for row in reader]
        csvfile.close()

    with open('girls.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        girl_pool = [Girl(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), row[5])\
                      for row in reader]
        csvfile.close()

    couples_list = []

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
					    datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='w')

    logging.info('\nFINDING SUITABLE MATCH FOR GIRLS\n')
    for girl in girl_pool:
        if girl.criteria == 'Attractive':
            boy_pool.sort(key=lambda x: x[1]).reverse()
        elif girl.criteria == 'Rich':
            boy_pool.sort(key=lambda x: x[2]).reverse()
        elif girl.criteria == 'Intelligent':
            boy_pool.sort(key=lambda x: x[3]).reverse()

        for boy in boy_pool:
            if boy.status == 'Single':
                logging.info('COURTING   :\t' + girl.name + ' is checking out ' + boy.name)
                if boy.check_elligibility(girl) and girl.check_elligibility(boy):
                    boy.match(girl)
                    girl.match(boy)
                    logging.info('MATCHED    :\t' + girl.name + ' is committed with ' + boy.name + '\n')
                    couples_list.append((boy, girl))
                    break

        if girl.status == 'Single':
            logging.info('UNMATCHED  :\t' + girl.name + ' could not find a suitable partner\n')

    print('COUPLES FORMED\n')
    for couple in couples_list:
        print(couple[1].name + '\t  AND\t' + couple[0].name)
