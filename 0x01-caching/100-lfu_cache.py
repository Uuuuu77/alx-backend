#!/usr/bin/env python3

""" LFU Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # discarding most recently used item
                lfu_key = [k for k, v in self.frequency.items() if v == min(
                    self.frequency.values()
                )]
                if len(lfu_key) > 1:
                    lru_key = min(lfu_key, key=lambda k: self.cache_data[k][1])
                else:
                    lru_key = lfu_key[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)

            # Adds new item
            self.cache_data[key] = (item, 1)
            self.frequency[key] = 1

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            # updating frequency list when item accessed
            self.frequency[key] += 1
            return self.cache_data[key][0]
        else:
            return None
