#!/usr/bin/python3
""" Create a class LRUCache that inherits
from BaseCaching and is a caching system """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system LRU caching """

    def __init__(self):
        """ Init method """
        super().__init__()
        self.itemList = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = self.getFirstItem(self.itemList)
            if first_item:
                self.itemList.pop(0)
                del self.cache_data[first_item]
                print("DISCARD: {}".format(first_item))

        if key not in self.itemList:
            self.itemList.append(key)
        else:
            self.moveToEndOfList(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.moveToEndOfList(key)
        return item

    def getFirstItem(array):
        """ returns item at index 0"""
        return array[0] if array else None

    def moveToEndOfList(self, item):
        """ Put element at the end of list """
        if self.itemList[len(self.itemList) - 1] != item:
            self.itemList.remove(item)
            self.itemList.append(item)
