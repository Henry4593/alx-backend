#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines a basic caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if not key or key is None:
            return None
        return self.cache_data.get(key, None)
