#!/usr/bin/env python3
'''the LIFOCache class module'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''this class inherits from BaseCaching'''

    def __init__(self):
        '''initializes the class'''
        super().__init__()

    def put(self, key, item):
        '''sets the key/value pair'''
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    last_key = list(self.cache_data.keys())[-1]
                    del self.cache_data[last_key]
                    print(f'DISCARD: {last_key}')
                elif key in self.cache_data.keys():
                    last_key = key
                    del self.cache_data[last_key]
                    print(f'DISCARD: {last_key}')
            self.cache_data[key] = item

    def get(self, key):
        '''retrieves the value of key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
