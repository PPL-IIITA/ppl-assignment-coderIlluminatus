'''ALL ALGORITHMIC OPERATIONS'''

import csv
import logging
import pickle

def get_boy_pool():
    '''GENERATES BOY OBJECT LIST FROM .csv FILE'''
    from boys.boy import Boy
    from boys.boy_miser import BoyMiser
    from boys.boy_generous import BoyGenerous
    from boys.boy_geek import BoyGeek

    with open('boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        boy_pool = []
        for row in reader:
            if row[5] == 'Miser':
                boy_pool.append(BoyMiser(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
            elif row[5] == 'Generous':
                boy_pool.append(BoyGenerous(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
            elif row[5] == 'Geek':
                boy_pool.append(BoyGeek(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
        csvfile.close()
    return boy_pool

def get_girl_pool():
    '''GENERATES GIRL OBJECT LIST FROM .csv FILE'''
    from girls.girl import Girl
    from girls.girl_choosy import GirlChoosy
    from girls.girl_normal import GirlNormal
    from girls.girl_desparate import GirlDesparate

    with open('girls.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        girl_pool = []
        for row in reader:
            if row[4] == 'Choosy':
                girl_pool.append(GirlChoosy(row[0], int(row[1]), int(row[2]), int(row[3]), row[5]))
            elif row[4] == 'Normal':
                girl_pool.append(GirlNormal(row[0], int(row[1]), int(row[2]), int(row[3]), row[5]))
            elif row[4] == 'Desparate':
                girl_pool.append(GirlDesparate(row[0], int(row[1]), int(row[2]), int(row[3]), row[5]))
        csvfile.close()
    return girl_pool

def get_gifts_list():
    '''GENERATES GIFT OBJECT LIST FROM .csv FILE'''
    from gifts.gift import Gift
    from gifts.gift_essential import GiftEssential
    from gifts.gift_luxury import GiftLuxury
    from gifts.gift_utility import GiftUtility

    gifts_list = []

    with open('gifts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            current_gift_type = row[3]
            if current_gift_type == 'Essential':
                gifts_list.append(GiftEssential(row[0], int(row[1]), int(row[2])))
            elif current_gift_type == 'Luxury':
                gifts_list.append(GiftLuxury(row[0], int(row[1]), int(row[2]), int(row[4]), int(row[5])))
            elif current_gift_type == 'Utility':
                gifts_list.append(GiftUtility(row[0], int(row[1]), int(row[2]), int(row[4]), int(row[5])))
        csvfile.close()
    return gifts_list

def make_couples(is_alternate):
    '''FORMS COUPLES BASED ON BUDGET AND MAINTENANCE CRITERIA'''
    boy_pool = get_boy_pool()
    girl_pool = get_girl_pool()

    if is_alternate:
        couples_list = pair_up_alternate(boy_pool, girl_pool)
    else:
        couples_list = pair_up(boy_pool, girl_pool)
    pickle.dump(couples_list, open("couple.p", "wb"))

def make_couples_secondary():
    '''FORMS COUPLES BASED ON SECONDARY CRITERIA'''
    boy_pool = get_boy_pool()
    girl_pool = get_girl_pool()

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='w')

    from top_k import TopK
    from couple import Couple
    couples_list = []

    logging.info('\n\nFINDING SUITABLE MATCH\n')
    i, j = 0, 0
    while i < len(girl_pool) or j < len(boy_pool):
        if i < len(girl_pool):
            while girl_pool[i].status == 'Committed' and i < len(girl_pool):
                i += 1
            if i == len(girl_pool):
                continue
            girl = girl_pool[i]
            new_boy_pool = TopK(boy_pool).get_top_k(len(boy_pool))
            if girl.criteria == 'Attractive':
                new_boy_pool.sort(key=lambda x: x.attr, reverse=True)
            elif girl.criteria == 'Rich':
                new_boy_pool.sort(key=lambda x: x.budget, reverse=True)
            elif girl.criteria == 'Intelligent':
                new_boy_pool.sort(key=lambda x: x.intel, reverse=True)

            for boy in new_boy_pool:
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
            i += 1

        if j < len(boy_pool):
            while boy_pool[i].status == 'Committed' and j < len(boy_pool):
                j += 1
            if j == len(boy_pool):
                continue
            boy = boy_pool[j]
            new_girl_pool = TopK(girl_pool).get_top_k(len(girl_pool))
            new_girl_pool.sort(key=lambda x: x.mcost, reverse=False)

            for girl in new_girl_pool:
                if girl.status == 'Single':
                    logging.info('COURTING   :\t' + boy.name + ' is checking out ' + girl.name)
                    if boy.check_elligibility(girl) and girl.check_elligibility(boy):
                        boy.match(girl)
                        girl.match(boy)
                        logging.info('MATCHED    :\t' + boy.name + ' is committed with ' + girl.name + '\n')
                        couples_list.append(Couple(boy, girl))
                        break

            if boy.status == 'Single':
                logging.info('UNMATCHED  :\t' + boy.name + ' could not find a suitable partner\n')
            j += 1

    print('COUPLES FORMED\n')
    if len(couples_list) >= 1:
        for couple in couples_list:
            print(couple.girl.name + '\t  AND\t' + couple.boy.name)
        print('\n\n')
    else:
        print('NO COUPLES FORMED.')

    pickle.dump(couples_list, open("couple.p", "wb"))

def make_couples_random():
    '''FORMS COUPLES BASED ON RANDOM PICK'''
    boy_pool = get_boy_pool()
    girl_pool = get_girl_pool()

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='w')

    from random_k import RandomK
    from couple import Couple
    couples_list = []

    logging.info('\n\nFINDING SUITABLE MATCH\n')
    i, j = 0, 0
    while i < len(girl_pool) or j < len(boy_pool):
        if i < len(girl_pool):
            while girl_pool[i].status == 'Committed' and i < len(girl_pool):
                i += 1
            if i == len(girl_pool):
                continue
            girl = girl_pool[i]

            boy = RandomK(boy_pool).get_random_k(len(boy_pool) - 1)
            if boy.status == 'Single':
                logging.info('COURTING   :\t' + girl.name + ' is checking out ' + boy.name)
                if boy.check_elligibility(girl) and girl.check_elligibility(boy):
                    boy.match(girl)
                    girl.match(boy)
                    logging.info('MATCHED    :\t' + girl.name + ' is committed with ' + boy.name + '\n')
                    couples_list.append(Couple(boy, girl))

            if girl.status == 'Single':
                logging.info('UNMATCHED  :\t' + girl.name + ' could not find a suitable partner\n')
            i += 1

        if j < len(boy_pool):
            while boy_pool[i].status == 'Committed' and j < len(boy_pool):
                j += 1
            if j == len(boy_pool):
                continue
            boy = boy_pool[j]
            boy = RandomK(boy_pool).get_random_k(len(boy_pool) - 1)

            if girl.status == 'Single':
                logging.info('COURTING   :\t' + boy.name + ' is checking out ' + girl.name)
                if boy.check_elligibility(girl) and girl.check_elligibility(boy):
                    boy.match(girl)
                    girl.match(boy)
                    logging.info('MATCHED    :\t' + boy.name + ' is committed with ' + girl.name + '\n')
                    couples_list.append(Couple(boy, girl))

            if boy.status == 'Single':
                logging.info('UNMATCHED  :\t' + boy.name + ' could not find a suitable partner\n')
            j += 1

    print('COUPLES FORMED\n')
    if len(couples_list) >= 1:
        for couple in couples_list:
            print(couple.girl.name + '\t  AND\t' + couple.boy.name)
        print('\n\n')
    else:
        print('NO COUPLES FORMED.')

    pickle.dump(couples_list, open("couple.p", "wb"))

def pair_up(boy_pool, girl_pool):
    '''PAIRS UP COUPLES FROM BOY POOL AND GIRL POOL WHERE GIRLS CHOOSE BOYS'''
    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='w')

    from couple import Couple
    couples_list = []

    logging.info('\n\nFINDING SUITABLE MATCH FOR GIRLS\n')
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

def pair_up_alternate(boy_pool, girl_pool):
    '''PAIRS UP COUPLES FROM BOY POOL AND GIRL POOL WHERE GIRLS AND BOYS CHOOSE PARTNERS ALTERNATELY'''
    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='w')

    boy_pool.sort(key=lambda x: x.attr, reverse=True)
    girl_pool.sort(key=lambda x: x.mcost, reverse=True)

    from couple import Couple
    couples_list = []

    logging.info('\n\nFINDING SUITABLE MATCH\n')
    i, j = 0, 0
    while i < len(girl_pool) or j < len(boy_pool):
        if i < len(girl_pool):
            while girl_pool[i].status == 'Committed':
                i += 1
                if i == len(girl_pool):
                    continue
            girl = girl_pool[i]
            if girl.criteria == 'Attractive':
                new_boy_pool = sorted(boy_pool, key=lambda x: x.attr, reverse=True)
            elif girl.criteria == 'Rich':
                new_boy_pool = sorted(boy_pool, key=lambda x: x.budget, reverse=True)
            elif girl.criteria == 'Intelligent':
                new_boy_pool = sorted(boy_pool, key=lambda x: x.intel, reverse=True)

            for boy in new_boy_pool:
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

        if j < len(boy_pool):
            while boy_pool[i].status == 'Committed':
                j += 1
                if j == len(boy_pool):
                    continue
            boy = boy_pool[j]

            for girl in girl_pool:
                if girl.status == 'Single':
                    logging.info('COURTING   :\t' + boy.name + ' is checking out ' + girl.name)
                    if boy.check_elligibility(girl) and girl.check_elligibility(boy):
                        boy.match(girl)
                        girl.match(boy)
                        logging.info('MATCHED    :\t' + boy.name + ' is committed with ' + girl.name + '\n')
                        couples_list.append(Couple(boy, girl))
                        break

            if boy.status == 'Single':
                logging.info('UNMATCHED  :\t' + boy.name + ' could not find a suitable partner\n')

    print('COUPLES FORMED\n')
    if len(couples_list) >= 1:
        for couple in couples_list:
            print(couple.girl.name + '\t  AND\t' + couple.boy.name)
        print('\n\n')
    else:
        print('NO COUPLES FORMED.')
    return couples_list

def give_gifts(couples_list, day_name, choice):
    '''BOYS GIVING GIFTS TO GIRLS'''

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='a')

    gifts_list = get_gifts_list()

    logging.info('\n\nGIFTING DATE : ' + day_name + '\n')
    for couple in couples_list:
        calculate_happiness(couple, gifts_list, choice)
    pickle.dump(couples_list, open("couple.p", "wb"))

def give_gifts_secondary(couples_list, day_name):
    '''BOYS GIVING GIFTS TO GIRLS BASED ON SECONDARY CRITERIA'''

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='a')

    gifts_list = get_gifts_list()

    logging.info('\n\nGIFTING DATE : ' + day_name + '\n')
    for couple in couples_list:
        calculate_happiness_secondary(couple, gifts_list)
    pickle.dump(couples_list, open("couple.p", "wb"))

def give_gifts_random(couples_list, day_name):
    '''BOYS GIVING GIFTS TO GIRLS BASED ON RANDOM PICKS'''

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='a')

    gifts_list = get_gifts_list()

    logging.info('\n\nGIFTING DATE : ' + day_name + '\n')
    for couple in couples_list:
        calculate_happiness_random(couple, gifts_list)
    pickle.dump(couples_list, open("couple.p", "wb"))

def select_gifts(couple, gifts_list):
    '''SELECTS GIFTS FOR A PARTICULAR COUPLE'''
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

def select_gifts_secondary(couple, gifts_list):
    '''SELECTS GIFTS FOR A PARTICULAR COUPLE BASED ON SECONDARY CRITERIA'''
    from top_k import TopK
    gifts_list = TopK(gifts_list).get_top_k(len(gifts_list))
    gifts_list.sort(key=lambda x: x.value, reverse=True)

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

def select_gifts_random(couple, gifts_list):
    '''SELECTS GIFTS FOR A PARTICULAR COUPLE BASED ON RANDOM PICK'''
    from random_k import RandomK

    #SPECIFYING FORMAT OF EVENT LOG
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',\
                        datefmt='%d/%m/%Y %I:%M:%S %p',\
                        level=logging.DEBUG,\
                        filename='eventlog.txt',\
                        filemode='a')

    logging.info('ENTERING  :\t' + couple.boy.name + ' and ' + couple.girl.name)
    total_cost, count_gifts = 0, 0
    while total_cost <= couple.boy.budget:
        gift = RandomK(gifts_list).get_random_k(len(gifts_list))
        couple.gift_basket.append(gift)
        logging.info('GIFTING   :\t' + couple.boy.name + ' is giving ' + gift.name + ' to ' + couple.girl.name)
        total_cost += gift.price
        count_gifts += 1

    logging.info('LEAVING   :\t' + couple.boy.name + ' and ' + couple.girl.name + '\n')

def calculate_happiness(couple, gifts_list, choice):
    '''CALCULATES HAPPINESS AND COMPATIBILITY OF COUPLE'''
    from selectors.selector import Selector
    from selectors.selector_any import SelectorAny
    from selectors.selector_every import SelectorEvery
    if choice == 'default':
        Selector(couple, gifts_list).select_gifts()
    elif choice == 'any':
        SelectorAny(couple, gifts_list).select_gifts()
    elif choice == 'every':
        SelectorEvery(couple, gifts_list).select_gifts()

    couple.girl.set_happiness(couple.gift_basket)
    couple.boy.set_happiness(couple.gift_basket)
    couple.set_happiness()
    couple.set_compatibility()

def calculate_happiness_secondary(couple, gifts_list):
    '''CALCULATES HAPPINESS AND COMPATIBILITY OF COUPLE USING SECONDARY CRITERIA GIFTING MECHANISM'''
    select_gifts_secondary(couple, gifts_list)

    couple.girl.set_happiness(couple.gift_basket)
    couple.boy.set_happiness(couple.gift_basket)
    couple.set_happiness()
    couple.set_compatibility()

def calculate_happiness_random(couple, gifts_list):
    '''CALCULATES HAPPINESS AND COMPATIBILITY OF COUPLE USING RANDOM PICK GIFTING MECHANISM'''
    select_gifts_random(couple, gifts_list)

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
    logging.info('\n\nENDING RELEATIONSHIPS\n')
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
    give_gifts(new_couples_list, 'Valentine\'s Day', 'default')
    pickle.dump(couples_list, open("couple.p", "wb"))
