#!/usr/bin/python3
"""This script creats  a class FIFOCache that inherits
from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Init method """
        super().__init__()
        self.cacheList = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data
        the item value for the key key """
        if key is None or item is None:
            return

        if key not in self.cacheList:
            self.cacheList.append(key)
        else:
            self.moveToEndOfList(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = self.getFirstItem(self.cacheList)
            if first_item:
                self.cacheList.pop(0)
                del self.cache_data[first_item]
                print("DISCARD: {}".format(first_item))

    def get(self, key):
        """returns the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)


    def getFirstItem(array):
        """ returns item at index 0"""
        return array[0] if array else None

    def moveToEndOfList(self, item):
        """ Put element at the end of list """
        if self.cacheList[len(self.cacheList) - 1] != item:
            self.cacheList.remove(item)
            self.cacheList.append(item)
