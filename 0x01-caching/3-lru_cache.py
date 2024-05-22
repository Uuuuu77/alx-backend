#!/usr/bin/env python3

""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Assign to dictionary self.cache_data the item value for the key key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # discarding least recently used item
                lru_key = self.order_used.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

            # Adds new item
            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            # Updating order list when item accessed
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        else:
            return None
