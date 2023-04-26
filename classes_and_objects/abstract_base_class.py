""" It has three abstract methods (len, getitem, and contains) that must be implemented by any subclass that
inherits from it. It also has three non-abstract methods: index, count, and contains."""

from abc import ABCMeta, abstractmethod
class Sequence(metaclass=ABCMeta):
    """This is our own version of abstract base class"""

    @abstractmethod
    def __len__(self):
        """returning the length of the sequence"""

    @abstractmethod
    def __getitem__(self):
        """return element at index j of the sequence"""

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found """
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
class MySequence(Sequence):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, j):
        return self.data[j]

seq = MySequence([1, 2, 3, 4, 5])
print(len(seq))    # Output: 5
print(seq[2])      # Output: 3
print(3 in seq)