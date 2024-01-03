#!/usr/bin/env python3
'''the MRUCache class module'''


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''this class inherits from BaseCaching'''

    def __init__(self):
        '''initializes the class'''
        super().__init__()
        self.mru_list = [] 

    def put(self, key, item):
        '''sets the key/value pair'''
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.mru_list:
                self.mru_list.remove(key)
            else:
                mru_key = self.mru_list.pop(-1)
                del self.cache_data[mru_key]
                print(f'DISCARD: {mru_key}')
        self.cache_data[key] = item
        self.mru_list.append(key)

    def get(self, key):
        '''retrieves the value of key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
