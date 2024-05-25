#!/usr/bin/python3

class CountedIterator:
    """
    A class that extends the built-in iterator obtained
    from the 'iter' function.
    It keeps track of the number of items that have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator class.

        Args:
            iterable (iterable): The iterable object to be iterated over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Override the '__next__' method to increment the counter
        and fetch the next item.

        Raises:
            StopIteration: If there are no more items to iterate over.

        Returns:
            The next item from the iterable.
        """
        self.count += 1
        return next(self.iterator)

    def get_count(self):
        """
        Return the current value of the counter.

        Returns:
            int: The number of items iterated over.
        """
        return self.count
