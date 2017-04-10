'''QUESTION 7'''

from random import sample

from partners.partner_linear import PartnerLinear
from partners.partner_binary import PartnerBinary
from partners.partner_hash import PartnerHash

from algorithms import get_boy_pool

boy_pool_size = len(get_boy_pool())
boy_num_list = sample(range(boy_pool_size), (boy_pool_size // 2))

boy_name_list = [('Boy ' + str(i)) for i in boy_num_list]
girl_name_list_linear = PartnerLinear(boy_name_list).get_girlfriend_name_linear_search()
girl_name_list_binary = PartnerBinary(boy_name_list).get_girlfriend_name_binary_search()
girl_name_list_hash = PartnerHash(boy_name_list).get_girlfriend_name_hash_table()

print('RESULTS FOR VARIOUS IMPLEMENTATIONS\n\n')
for i in range(len(boy_name_list)):
    print('BOY NAME\t:\t', boy_name_list[i])
    print('LINKED LIST\t:\t', girl_name_list_linear[i])
    print('BINARY SEARCH\t:\t', girl_name_list_binary[i])
    print('HASH TABLE\t:\t', girl_name_list_hash[i])
    print('\n')
