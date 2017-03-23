'''ALL ALGORITHMIC OPERATIONS'''

import csv
import logging
import pickle

def make_couples(is_inherited):
    '''FORMS COUPLES BASED ON BUDGET AND MAINTENANCE CRITERIA'''
    if is_inherited:
        from boys.boy import Boy
        from boys.boy_miser import BoyMiser
        from boys.boy_generous import BoyGenerous
        from boys.boy_geek import BoyGeek

        from girls.girl import Girl
        from girls.girl_choosy import GirlChoosy
        from girls.girl_normal import GirlNormal
        from girls.girl_desparate import GirlDesparate

    else:
        from boys.boy_uninherited import Boy
        from girls.girl_uninherited import Girl

    with open('boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if is_inherited:
            boy_pool = []
            for row in reader:
                if row[5] == 'Miser':
                    boy_pool.append(BoyMiser(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
                elif row[5] == 'Generous':
                    boy_pool.append(BoyGenerous(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
                elif row[5] == 'Geek':
                    boy_pool.append(BoyGeek(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
        else:
            boy_pool = [Boy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), row[5])\
                        for row in reader]
        csvfile.close()

    with open('girls.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if is_inherited:
            girl_pool = []
            for row in reader:
                if row[4] == 'Choosy':
                    girl_pool.append(GirlChoosy(row[0], int(row[1]), int(row[2]), int(row[3]), row[5]))
                elif row[4] == 'Normal':
                    girl_pool.append(GirlNormal(row[0], int(row[1]), int(row[2]), int(row[3]), row[5]))
                elif row[4] == 'Desparate':
                    girl_pool.append(GirlDesparate(row[0], int(row[1]), int(row[2]), int(row[3]), row[5]))
        else:
            girl_pool = [Girl(row[0], int(row[1]), int(row[2]), int(row[3]), row[4], row[5])\
                        for row in reader]
        csvfile.close()

    couples_list = pair_up(boy_pool, girl_pool)
    pickle.dump(couples_list, open("couple.p", "wb"))

def pair_up(boy_pool, girl_pool):
    '''PAIRS UP COUPLES FROM BOY POOL AND GIRL POOL'''
    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='w')

    from couple import Couple
    couples_list = []

    logging.info('\nFINDING SUITABLE MATCH FOR GIRLS\n')
    for girl in girl_pool:
        if girl.criteria == 'Attractive':
            boy_pool.sort(key=lambda x: x.attr, reverse=True)
        elif girl.criteria == 'Rich':
            boy_pool.sort(key=lambda x: x.budget, reverse=True)
        elif girl.criteria == 'Intelligent':
            boy_pool.sort(key=lambda x: x.intel, reverse=True)

        for boy in boy_pool:
            if boy.status == 'Single':
                logging.info('COURTING   :\t' + girl.name + ' is checking out ' + boy.name)
                if boy.check_elligibility(girl) and girl.check_elligibility(boy):
                    boy.match(girl)
                    girl.match(boy)
                    logging.info('MATCHED    :\t' + girl.name + ' is committed with ' + boy.name + '\n')
                    couples_list.append(Couple(boy, girl))
                    break

        if girl.status == 'Single':
            logging.info('UNMATCHED  :\t' + girl.name + ' could not find a suitable partner\n')

    print('COUPLES FORMED\n')
    if len(couples_list) >= 1:
        for couple in couples_list:
            print(couple.girl.name + '\t  AND\t' + couple.boy.name)
        print('\n\n')
    else:
        print('NO COUPLES FORMED.')
    return couples_list

def give_gifts(is_inherited, couples_list):
    '''BOYS GIVING GIFTS TO GIRLS'''
    if is_inherited:
        from gifts.gift import Gift
        from gifts.gift_essential import GiftEssential
        from gifts.gift_luxury import GiftLuxury
        from gifts.gift_utility import GiftUtility
    else:
        from gifts.gift_uninherited import Gift

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='a')

    gifts_list = []

    with open('gifts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            current_gift_type = row[3]
            if is_inherited:
                if current_gift_type == 'Essential':
                    gifts_list.append(GiftEssential(row[0], int(row[1]), int(row[2])))
                elif current_gift_type == 'Luxury':
                    gifts_list.append(GiftLuxury(row[0], int(row[1]), int(row[2]), int(row[4]), int(row[5])))
                elif current_gift_type == 'Utility':
                    gifts_list.append(GiftUtility(row[0], int(row[1]), int(row[2]), int(row[4]), int(row[5])))
            else:
                if current_gift_type == 'Essential':
                    gifts_list.append(Gift(row[0], int(row[1]), int(row[2]), row[3], 0, 0, 0, 0))
                elif current_gift_type == 'Luxury':
                    gifts_list.append(Gift(row[0], int(row[1]), int(row[2]), row[3], int(row[4]), int(row[5]), 0, 0))
                elif current_gift_type == 'Utility':
                    gifts_list.append(Gift(row[0], int(row[1]), int(row[2]), row[3], 0, 0, int(row[4]), int(row[5])))
        csvfile.close()

    logging.info('\n\nGIFTING DATE : Valentine\'s Day\n')
    for couple in couples_list:
        calculate_happiness(couple, gifts_list)
    pickle.dump(couples_list, open("couple.p", "wb"))

def calculate_happiness(couple, gifts_list):
    '''CALCULATES HAPPINESS AND COMPATIBILITY OF COUPLE'''

    if couple.get_boy_nature() == 'Generous':
        gifts_list.sort(key=lambda x: x.price, reverse=True)
    else:
        gifts_list.sort(key=lambda x: x.price)

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='a')

    logging.info('ENTERING  :\t' + couple.boy.name + ' and ' + couple.girl.name)
    total_cost, count_gifts, pos = 0, 0, 0
    for gift in gifts_list:
        if total_cost + gift.price >= couple.boy.budget:
            if couple.get_boy_nature() != 'Generous':
                couple.gift_basket.append(gift)
                logging.info('GIFTING   :\t' + couple.boy.name + ' is giving ' + gift.name + ' to ' + couple.girl.name)
                total_cost += gift.price
                count_gifts += 1

            #A GEEK BOY CHECKS FOR AN ADDITIONAL LUXURY GIFT, IF BUDGET PERMITS
            if couple.get_boy_nature() == 'Geek' and total_cost < couple.boy.budget:
                for gift_index in range(pos + 1, len(gifts_list)):
                    if gifts_list[gift_index].nature == 'Luxury' and total_cost + gifts_list[gift_index] <= couple.boy.budget:
                        logging.info('GIFTING   :\t' + couple.boy.name + ' is giving ' + gift.name + ' to ' + couple.girl.name + ' (Additional Luxury Gift)')
                        total_cost += gift.price
                        count_gifts += 1
            pos += 1
            break
        couple.gift_basket.append(gift)
        logging.info('GIFTING   :\t' + couple.boy.name + ' is giving ' + gift.name + ' to ' + couple.girl.name)
        total_cost += gift.price
        count_gifts += 1

    #INCREASE BUDGET WHERE GIFTING IS NOT POSSIBLE
    if count_gifts == 0:
        couple.boy.budget = min(gift.price for gift in gifts_list)
        for gift in gifts_list:
            if couple.boy.budget == gift.price:
                logging.info('GIFTING   :\t' + couple.boy.name + ' is giving ' + gift.name + ' to ' + couple.girl.name)
                couple.gift_basket.append(gift)
                break
    logging.info('LEAVING   :\t' + couple.boy.name + ' and ' + couple.girl.name + '\n')

    couple.girl.set_happiness(couple.gift_basket)
    couple.boy.set_happiness(couple.gift_basket)
    couple.set_happiness()
    couple.set_compatibility()

def print_gifts(couples_list):
    '''DISPLAYS EXCHANGED GIFTS FOR EACH COUPLE'''
    for couple in couples_list:
        print('GIFTS EXCHANGED BETWEEN ' + couple.boy.name + ' AND ' + couple.girl.name)
        print('BOY \nNATURE      : ' + couple.get_boy_nature() + '\nBUDGET      : ' + str(couple.boy.budget))
        print('\nGIRL \nNATURE      : ' + couple.get_girl_nature() + '\nMAINTENANCE : ' + str(couple.girl.mcost) + '\n')
        for gift in couple.gift_basket:
            print(gift.name + '  \t' + 'PRICE = ' + str(gift.price) + '\tVALUE = ' + str(gift.value))
        print('\n\n')

def print_happy_couples(couples_list, k):
    '''DISPLAYS k MOST HAPPY COUPLES'''
    print('\n' + str(k) + ' MOST HAPPY COUPLES :')
    happy_list = sorted(couples_list, key=lambda x: x.happiness, reverse=True)
    for i in range(k):
        print(happy_list[i].girl.name + '\t  AND\t' + happy_list[i].boy.name + '\tHAPPINESS    \t=\t' + str(happy_list[i].happiness))

def print_compatible_couples(couples_list, k):
    '''DISPLAYS k MOST COMPATIBLE COUPLES'''
    print('\n' + str(k) + ' MOST COMPATIBLE COUPLES :')
    compatible_list = sorted(couples_list, key=lambda x: x.compatibility, reverse=True)
    for i in range(k):
        print(compatible_list[i].girl.name + '\t  AND\t' + compatible_list[i].boy.name + '\tCOMPATIBILITY\t=\t' + str(compatible_list[i].compatibility))

def move_on(couples_list, k):
    '''BREAKS UP k LEAST HAPPY COUPLES AND ASSIGNS THEM NEW PARTNERS'''
    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='a')
    unhappy_list = sorted(couples_list, key=lambda x: x.happiness)
    print('\nBREAKING UP ' + str(k) + ' LEAST HAPPY COUPLES :')
    boys_broken, girls_broken = [], []
    for i in range(k):
        logging.info('BREAKING UP  :\t' + unhappy_list[i].boy.name + ' and ' + unhappy_list[i].girl.name)
        unhappy_list[i].break_up()
        boys_broken.append(unhappy_list[i].boy)
        girls_broken.append(unhappy_list[i].girl)
        couples_list.remove(unhappy_list[i])
    print('\n\n')
    new_couples_list = pair_up(boys_broken, girls_broken)
    couples_list = couples_list + new_couples_list
    give_gifts(True, new_couples_list)
    print_happy_couples(new_couples_list, len(couples_list))
    pickle.dump(couples_list, open("couple.p", "wb"))
