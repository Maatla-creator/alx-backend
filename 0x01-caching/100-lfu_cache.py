#!/usr/bin/python3
""" This script creates a class LFUCache that inherits
from BaseCaching and is a caching system """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Init method """
        super().__init__()
        self.cacheList = []
        self.counter = {}

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key key. """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.getFirstItem(self.cacheList)
            if first:
                self.cacheList.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.cacheList:
            self.cacheList.insert(0, key)
        self.moveItemToRight(key)

    def get(self, key):
        """ returns the value in self.cache_data linked to key. """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.moveItemToRight(key)
        return item

    def moveItemToRight(self, item):
        """ Moves element to the right  """
        length = len(self.cacheList)

        index = self.cacheList.index(item)
        item_count = self.counter[item]

        for i in range(index, length):
            if i != (length - 1):
                next = self.cacheList[i + 1]
                next_count = self.counter[next]

                if next_count > item_count:
                    break

        self.cacheList.insert(i + 1, item)
        self.cacheList.remove(item)

    def getFirstItem(array):
        """ returns item at index 0"""
        return array[0] if array else None
