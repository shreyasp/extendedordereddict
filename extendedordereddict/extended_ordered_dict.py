#!/usr/bin/python

from collections import OrderedDict


class ExtendedOrderedDict(OrderedDict):

    # Override to instantiate Order Indices list
    def __new__(cls, *args, **kwargs):
        _instance = OrderedDict.__new__(cls, *args, **kwargs)
        _instance.__order_index = list()
        return _instance

    # Overriding __setitem__, to append each new key to the Order Indices list
    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        super(ExtendedOrderedDict, self).__setitem__(key, value)
        self.__order_index.append(key)
        # TODO: Remove after final commit
        # print(self.__order_index)
        return self

    def print(self):
        pass

    def print_at_index(self, index):
        pass

    def insert_at_index(self, index):
        pass

    def insert_before_index(self, index):
        pass

    def insert_after_index(self, index):
        pass


if __name__ == '__main__':
    # e1 = ExtendedOrderedDict({'a': 'apple', 'b': 'ball'})
    # e2 = ExtendedOrderedDict(a='apple', b='ball', c='cat')
    e3 = ExtendedOrderedDict.fromkeys('a', 'apple')
