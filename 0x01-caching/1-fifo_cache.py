#!/usr/bin/env python3

""" FIFO caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            # Adds new item
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None:
            return self.cache_data.get(key)
