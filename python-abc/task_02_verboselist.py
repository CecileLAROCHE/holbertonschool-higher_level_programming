#!/usr/bin/env python3
"""
This module defines the VerboseList class
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        n = len(iterable)
        print(f"Extended the list with [{n}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Remove [{item}] from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Poppes [{item}] from the list.")
        return item
