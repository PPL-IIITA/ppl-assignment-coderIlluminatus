'''BINARY SEARCH IMPLEMENTATION OF PARTNER'''

from partners.partner import Partner

class PartnerBinary(Partner):

    '''USES INHERITANCE'''

    def __init__(self, boy_name_list):
        '''DEFAULT CONSTRUCTOR'''
        super(PartnerBinary, self).__init__(boy_name_list)

    def get_girlfriend_name_binary_search(self):
        '''RETURNS GIRLFRIEND NAME LIST USING BINARY SEARCH IMPLEMENTATION'''
        super(PartnerBinary, self).generate_committed_boy_pool()
        self.committed_boy_pool.sort(key=lambda x: x.name)
        for boy_name in self.boy_name_list:
            has_girlfriend = False
            low, high = 0, len(self.committed_boy_pool) - 1
            while low <= high:
                mid = (high + low) // 2
                if self.committed_boy_pool[mid].name == boy_name:
                    has_girlfriend = True
                    self.girl_name_list.append(self.committed_boy_pool[mid].partner.name)
                    break
                elif self.committed_boy_pool[mid].name > boy_name:
                    high = mid - 1
                else:
                    low = mid + 1
            if not has_girlfriend:
                self.girl_name_list.append('NO GIRLFRIEND')
        return self.girl_name_list
