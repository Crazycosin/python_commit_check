class QueueBuiltByTwoStacks(object):
    """Queue class which is built by two stacks

    When an item put into queue,put_stack store the item. when the queue
    get an item, if get_stack is not empty, get_stack pop the pop value,
    if two stacks are empty, return error, if get_stack is empty, but
    put_stack is not, firstly pop all items from put_stack to get_stack,
    and pop get_stack.
    """
    def __init__(self):
        self._put_stack = list()
        self._get_stack = list()

    def put(self, item):
        """This is a function of putting item into queue.

        Args:
            item (Any): An item will be added into queue.
        """
        self._put_stack.append(item)

    def get(self):
        """This is a function of getting item from queue

        Returns:
            Any: An item from the queue.
        """
        assert (self._put_stack
                or self._get_stack), ("Can't get an item from empty queue!")
        if self._get_stack:
            return self._get_stack.pop()
        while self._put_stack:
            self._get_stack.append(self._put_stack.pop())
        return self._get_stack.pop()

    def empty(self):
        """This is a function of judging whether the queue is empty.

        Returns:
            bool: True if the queue is empty.
        """
        return False if self._put_stack or self._get_stack else True

    def __len__(self):
        """This is a python's magic method.

        Returns:
            int: the length of the queue
        Examples:
            >>> queue = QueueBuiltByTwoStacks()
            >>> queue.put(3)
            >>> len(queue)
            1
        """
        return len(self._put_stack) + len(self._get_stack)

    def __repr__(self):
        """This is a python's magic method.

        Examples:
            >>> queue = QueueBuiltByTwoStacks()
            >>> queue.put(3)
            >>> print(queue)
            'queue of length 1'
        """
        return f'queue of length {len(self)}'
