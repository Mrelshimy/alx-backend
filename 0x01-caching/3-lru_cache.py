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
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.access_list:
                self.access_list.append(key)
            else:
                self.access_list.append(
                    self.access_list.pop(
                        self.access_list.index(key)
                    )
                )
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed_item = self.access_list.pop(0)
                del self.cache_data[removed_item]
                print("DISCARD: {}".format(removed_item))

    def get(self, key):
        """ get item of key from cache.data """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
