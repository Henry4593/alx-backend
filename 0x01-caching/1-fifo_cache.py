#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if not key or key is None:
            return None
        return self.cache_data.get(key, None)
