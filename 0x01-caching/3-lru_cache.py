#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class
    """
    def __init__(self):
        """ Initialize LRUCache
        """
        super().__init__()
        self.order = []

    def update_order(self, key):
        """ Update the order of the keys based on LRU
        """
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.update_order(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.update_order(key)
        return self.cache_data[key]
