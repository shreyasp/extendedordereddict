# extendedordereddict
Extended functionality for Python's Ordered Dict


```
from extendedordereddict import ExtendedOrderedDict

ex_od = ExtendedOrderedDict({'u': 'Uber'}, a='Apple', g='Google', m='Microsoft')

# Print in order
print(ex_od) # ExtendedOrderedDict([('u', 'Uber'), ('a', 'Apple'), ('g', 'Google'), ('m', 'Microsoft')])

# Print at Index
ex_od.print_at_index(1) # Apple

# At Index
ex_od.insert_at_index(1, {'x': 'Xerox'})
ex_od.print_at_index(1) # Xerox
ex_od.print_at_index(2) # Apple

# Before Index
ex_od.insert_before_index(2, {'d': 'Dropbox'})
ex_od.print_at_index(1) # Dropbox
ex_od.print_at_index(2) # Xerox

# After Index
ex_od.insert_after_index(2, {'i': 'Instagram'})
ex_od.print_at_index(2) # Xerox
ex_od.print_at_index(3) # Instagram

```
