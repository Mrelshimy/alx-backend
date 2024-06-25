#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache Class"""

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
            self.access_dict += 1
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            LF_key = list(sorted(self.access_dict))[0]
            print(f"DISCARD: {LF_key}")
            del self.cache_data[LF_key]
            self.access_dict[LF_key]
        self.access_dict[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """ get item of key from cache.data """
        if key is not None and key in self.cache_data.keys():
            self.access_dict[key] += 1
            return self.cache_data.get(key)
        return None
