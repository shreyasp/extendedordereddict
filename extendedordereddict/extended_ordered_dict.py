#!/usr/bin/python

from collections import OrderedDict


class ExtendedOrderedDict(OrderedDict):

    # Override to instantiate Order Indices list
    def __new__(cls, *args, **kwargs):
        __instance = OrderedDict.__new__(cls, *args, **kwargs)
        __instance.__items = list()
        __instance.__uniq_items = set()
        return __instance

    # Overriding __setitem__, to append each new key to the Order Indices list
    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        super(ExtendedOrderedDict, self).__setitem__(key, value)

        if key not in self.__uniq_items:
            self.__uniq_items.add(key)
            self.__items.append(key)

        return self

    def __delitem__(self, key, dict_delitem=dict.__delitem__):
        super(ExtendedOrderedDict, self).__delitem__(key)
        self.__items.remove(key)
        return self

    def __repr__(self):
        if not len(self.items()):
            return '%s()' % (self.__class__.__name__,)

        return '%s(%r)' % (self.__class__.__name__, self.items())

    def __update_items(self, index, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('Needs object to inserted at given position')

        keys = list()
        to_update = dict()
        if args:
            obj = args[0]
            keys.extend(obj.keys())
            to_update.update(obj)

        if kwargs:
            to_update = kwargs
            keys = list(to_update.keys())  # Returns dict_keys

        if(len(keys) > 1):
            raise Exception('Cannot insert multiple keys at same index')

        self.update(to_update)

        # If key is not already present add to set and update items
        # otherwise update the key position to new index
        if keys[0] not in self.__uniq_items:
            self.__uniq_items.add(keys[0])
            self.__items.insert(index, keys[0])

        else:
            self.__items.remove(keys[0])
            self.__items.insert(index, keys[0])

    def iteritems(self):
        for key in self.__items:
            yield (key, self.get(key))

    def popitem(self, last=True):
        if last:
            key = self.__items[-1]

        else:
            key = self.__items[0]

        value = self.pop(key)
        return key, value

    def items(self):
        return [(item, self.get(item)) for item in self.__items]

    def keys(self):
        return self.__items

    def values(self):
        return [self.get(key) for key in self.__items]

    def print_at_index(self, index):
        try:
            _item = self.__items[index]
            print(self.get(_item))

        except IndexError as error:
            raise(error)

    def get_at_index(self, index):
        print(self.__items)

        try:
            key = self.__items[index]

        except IndexError as error:
            raise(error)

        return self.get(key)

    def insert_at_index(self, index, *args, **kwargs):
        self.__update_items(index, *args, **kwargs)

    def insert_before_index(self, index, *args, **kwargs):
        actual_index = index - 1
        self.__update_items(actual_index, *args, **kwargs)

    def insert_after_index(self, index, *args, **kwargs):
        actual_index = index + 1
        self.__update_items(actual_index, *args, **kwargs)
