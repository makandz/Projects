# https://leetcode.com/problems/map-sum-pairs/

class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._values = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self._values[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for idx, (key, val) in enumerate(self._values.items()):
            if key.startswith(prefix):
                total += val
        return total