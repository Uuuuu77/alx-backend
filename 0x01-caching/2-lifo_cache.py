#!/usr/bin/env python3

""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # discarding the last item if cache is full
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

        # Adds new item
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None:
            return self.cache_data.get(key)
