#!/usr/bin/python3
""" This script creates a class BasicCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
        the item value for the key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
