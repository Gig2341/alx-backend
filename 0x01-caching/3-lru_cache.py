#!/usr/bin/env python3
'''the LRUCache class module'''


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''this class inherits from BaseCaching'''

    def __init__(self):
        '''initializes the class'''
        super().__init__()
        self.lru_list = [] 

    def put(self, key, item):
        '''sets the key/value pair'''
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.lru_list:
                self.lru_list.remove(key)
            else:
                lru_key = self.lru_list.pop(0)
                del self.cache_data[lru_key]
                print(f'DISCARD: {lru_key}')
        self.cache_data[key] = item
        self.lru_list.append(key)

    def get(self, key):
        '''retrieves the value of key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
