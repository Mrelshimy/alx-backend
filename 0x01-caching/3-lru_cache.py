#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache Class"""

    def __init__(self):
        """ Inistantiation method """
        super().__init__()
        self.access_dict = {}

    def put(self, key, item):
        """ Add key, Item to cache.data """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_dict[key] += 1
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            LR_key = list(sorted(self.access_dict))[0]
            print(f"DISCARD: {LR_key}")
            del self.cache_data[LR_key]
            del self.access_dict[LR_key]
        self.access_dict[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """ get item of key from cache.data """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
