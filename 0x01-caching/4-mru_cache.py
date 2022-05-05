#!/usr/bin/python3
""" This script creates a class MRUCache that inherits from BaseCaching
and is a caching system: """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching MRU system"""

    def __init__(self):
        """ Init Method """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ assigns to the dictionary self.cache_data
        the item value for the key key. """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.moveToEndOfList(key)

    def get(self, key):
        """ returns the value in self.cache_data linked to key. """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.moveToEndOfList(key)
        return item

    def moveToEndOfList(self, item):
        """ Put element at the end of list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)
