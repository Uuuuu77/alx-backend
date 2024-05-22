#!/usr/bin/env python3

""" Basic dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """

    def put(self, key, item):
        """ Assign to dictionary self.cache_data the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None:
            return self.cache_data.get(key)
