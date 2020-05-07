"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/813/

Insert Delete GetRandom O(1)

Design a data structure that supports all following operations
in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element
must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
from random import choice


class RandomizedSet:
    """
    Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    param_1 = obj.insert(val)
    param_2 = obj.remove(val)
    param_3 = obj.getRandom()
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        self.a = []
        self.deleted = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        if val in self.s:
            return False
        else:
            self.s.add(val)
            self.a.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        """
        if val in self.s:
            self.s -= {val}
            return True
            if 5*self.deleted > len(self.a):
                self.a = list(self.s)
            else:
                self.deleted += 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        for i in range(5):
            if (x: = choice(self.a)) in self.s: # noqa
                return x
        self.a = list(self.s)
        return choice(self.a)
