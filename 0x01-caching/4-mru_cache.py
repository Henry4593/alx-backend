#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a MRU caching system
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
                most_recently_used_key = self.order.pop()
                del self.cache_data[most_recently_used_key]
                print(f"DISCARD: {most_recently_used_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
