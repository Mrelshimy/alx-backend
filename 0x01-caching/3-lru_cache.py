#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache Class"""

    def __init__(self):
        """ Inistantiation method """
        super().__init__()
        self.access_list = []

    def put(self, key, item):
        """ Add key, Item to cache.data """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_list.append(
                self.access_list.pop(self.access_list.index(key)))
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            LR_key = self.access_list[0]
            print(f"DISCARD: {LR_key}")
            del self.cache_data[LR_key]
            self.access_list.pop(0)
        self.access_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get item of key from cache.data """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
