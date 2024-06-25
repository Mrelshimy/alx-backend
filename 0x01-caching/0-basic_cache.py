#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache Class """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add key, Item to cache.data """
        if key == None or item == None:
            return
        self.cache_data[key] = item
    
    def get(self, key):
        """ get item of key from cache.data """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
