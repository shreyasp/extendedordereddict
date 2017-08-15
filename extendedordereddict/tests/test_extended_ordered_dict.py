from unittest import TestCase
from extendedordereddict.extended_ordered_dict import ExtendedOrderedDict


class TestExtendedOrderedDict(TestCase):

    def test_extended_ordered_dict_type(self):
        ex_od = ExtendedOrderedDict()
        self.assertEqual(type(ex_od), ExtendedOrderedDict)

    def test_extended_ordered_dict_items(self):
        ex_od = ExtendedOrderedDict(a='Apple', g='Google', m='Microsoft')
        tester_dict = dict(a='Apple', g='Google', m='Microsoft')

        # TODO Need to implement _mapping for utilizing ItemsView() for
        # ExtendedOrderedDict
        tester_items = list(tester_dict.items())
        ex_od_items = ex_od.items()

        self.assertEqual(tester_items, ex_od_items)

    def test_extended_ordered_dict_keys(self):
        ex_od = ExtendedOrderedDict(a='Apple', g='Google', m='Microsoft')
        tester_dict = dict(a='Apple', g='Google', m='Microsoft')

        # TODO Need to implement _mapping for utilizing KeysView() for
        # ExtendedOrderedDict
        tester_items = list(tester_dict.keys())
        ex_od_items = ex_od.keys()

        self.assertEqual(tester_items, ex_od_items)

    def test_extended_ordered_dict_values(self):
        ex_od = ExtendedOrderedDict(a='Apple', g='Google', m='Microsoft')
        tester_dict = dict(a='Apple', g='Google', m='Microsoft')

        # TODO Need to implement _mapping for utilizing ValuesView() for
        # ExtendedOrderedDict
        tester_items = list(tester_dict.values())
        ex_od_items = ex_od.values()

        self.assertEqual(tester_items, ex_od_items)

    # TODO: Test cases for insertion at/before/after index to be written
