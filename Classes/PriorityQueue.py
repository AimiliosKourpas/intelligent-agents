from heapq import heappop, heappush, heapify

class PriorityQueue:
    """
    A priority queue where the item with the minimum or maximum priority (determined by the function f and order)
    is returned first.
    - If order is 'min', the item with the minimum f(x) is returned first.
    - If order is 'max', the item with the maximum f(x) is returned first.
    """

    def __init__(self, order='min', f=lambda x: x):
        """
        Initialize a PriorityQueue.
        :param order: 'min' for a min-heap, 'max' for a max-heap.
        :param f: A function that computes the priority of an item.
        """
        self.heap = []
        if order == 'min':
            self.f = f
        elif order == 'max':
            self.f = lambda x: -f(x)
        else:
            raise ValueError("Order must be either 'min' or 'max'.")

    def append(self, item):
        """
        Insert an item into the priority queue.
        :param item: The item to be inserted.
        """
        heappush(self.heap, (self.f(item), item))

    def extend(self, items):
        """
        Insert multiple items into the priority queue.
        :param items: An iterable of items to be inserted.
        """
        for item in items:
            heappush(self.heap, (self.f(item), item))

    def pop(self):
        """
        Remove and return the item with the highest priority (minimum or maximum).
        :return: The item with the highest priority.
        """
        if self.heap:
            return heappop(self.heap)[1]
        else:
            raise IndexError('Trying to pop from an empty PriorityQueue.')

    def __len__(self):
        """
        Return the number of items in the priority queue.
        :return: The number of items.
        """
        return len(self.heap)

    def __contains__(self, item):
        """
        Check if an item is in the priority queue.
        :param item: The item to check.
        :return: True if the item is in the queue, False otherwise.
        """
        return any(element == item for _, element in self.heap)

    def __getitem__(self, key):
        """
        Get an item from the priority queue.
        :param key: The item to retrieve.
        :return: The item if it exists, otherwise raises KeyError.
        """
        for _, item in self.heap:
            if item == key:
                return item
        raise KeyError(f"Item {key} not found in the PriorityQueue.")

    def __delitem__(self, key):
        """
        Delete the first occurrence of an item from the priority queue.
        :param key: The item to delete.
        """
        for i, (priority, item) in enumerate(self.heap):
            if item == key:
                del self.heap[i]
                heapify(self.heap)
                return
        raise KeyError(f"Item {key} not found in the PriorityQueue.")
