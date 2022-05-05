#!/usr/bin/python3
"""This script creates a class LIFOCache that inherits
from BaseCaching and is a caching system"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Init method """
        super().__init__()
        self.cacheList = []

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.cacheList:
                last_item_index = self.cacheList.pop()
                del self.cache_data[last_item_index]
                print("DISCARD: {}".format(last_item_index))

        if key not in self.cacheList:
            self.cacheList.append(key)
        else:
            self.moveToEndOfList(key)

    def get(self, key):
        """ returns the value in self.cache_data linked to key. """
        return self.cache_data.get(key, None)

    def moveToEndOfList(self, item):
        """ Put element at the end of list """
        if self.cacheList[len(self.cacheList) - 1] != item:
            self.cacheList.remove(item)
            self.cacheList.append(item)
