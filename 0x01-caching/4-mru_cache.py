#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache with MRU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the most recently used key (last item in the sorted order)
            mru_key = max(self.cache_data, key=self.cache_data.get)
            print("DISCARD: {}".format(mru_key))
            del self.cache_data[mru_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
