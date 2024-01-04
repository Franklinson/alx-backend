#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A simple caching system that inherits from BaseCaching.
    Implements the LFU (Least Frequently Used) eviction strategy
    with LRU (Least Recently Used) tie-breaking.
    """

    def __init__(self):
        """Constructor method initializing the cache and frequency counter."""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Put an item into the cache using LFU eviction strategy."""
        if key is None or item is None:
            return

        cache_len = len(self.cache_data)
        if key not in self.cache_data:
            if cache_len + 1 > BaseCaching.MAX_ITEMS:
                least_freq_key = min(self.frequency,
                                     key=lambda k: self.frequency[k])
                print("DISCARD: {}".format(least_freq_key))
                del self.cache_data[least_freq_key]
                del self.frequency[least_freq_key]

        self.cache_data[key] = item
        self.frequency[key] = 0

    def get(self, key):
        """Get an item from the cache, updating its frequency."""
        if key is None or key not in self.cache_data:
            return None

        val = self.cache_data.pop(key)
        self.cache_data[key] = val
        self.frequency[key] += 1
        return val
