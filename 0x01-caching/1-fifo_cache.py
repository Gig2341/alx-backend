#!/usr/bin/env python3
'''the FIFOCache class module'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''this class inherits from BaseCaching'''

    def __init__(self):
        '''initializes the class'''
        super().__init__()

    def put(self, key, item):
        '''sets the key/value pair'''
        if key is None or item is None:
            pass
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.cache_data.pop(0)        
            print(f'DISCARD: {key}')
        self.cache_data[key] = item


    def get(self, key):
        '''retrieves the value of key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
