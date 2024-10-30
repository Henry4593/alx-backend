#!/usr/bin/env python3
"""
LFUCache module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache defines a LFU caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)
        self.usage = defaultdict(OrderedDict)

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_freq = min(self.usage.keys())
                    lfu_key, _ = self.usage[min_freq].popitem(last=False)
                    if not self.usage[min_freq]:
                        del self.usage[min_freq]
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    print(f"DISCARD: {lfu_key}")
                self.cache_data[key] = item
                self.frequency[key] = 1
            self._update_usage(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self._update_usage(key)
        return self.cache_data[key]

    def _update_usage(self, key):
        """
        Update the usage frequency of a key
        """
        freq = self.frequency[key]
        if freq > 1:
            del self.usage[freq - 1][key]
            if not self.usage[freq - 1]:
                del self.usage[freq - 1]
        self.usage[freq][key] = None
