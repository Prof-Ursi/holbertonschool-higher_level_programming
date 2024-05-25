#!/usr/bin/python3

class VerboseList(list):
    """
    A custom list class that extends the built-in list class
    with verbose notifications for modifications.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification message.

        Args:
            item: The item to be appended to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable
        and print a notification message.

        Args:
            iterable: An iterable containing items to extend the list.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification message.

        Args:
            item: The item to be removed from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item from the list and print a notification message.

        Args:
            index: The index of the item to pop from the list.
            Defaults to the last item.

        Returns:
            The popped item.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
