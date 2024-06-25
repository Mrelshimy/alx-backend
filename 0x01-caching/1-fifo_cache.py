#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache Class"""

    def __init__(self):
        """ Inistantiation method """
        super().__init__()

    def put(self, key, item):
        """ Add key, Item to cache.data """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            print(f"DISCARD: {oldest_key}")
            del self.cache_data[oldest_key]
        self.cache_data[key] = item

    def get(self, key):
        """ get item of key from cache.data """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
