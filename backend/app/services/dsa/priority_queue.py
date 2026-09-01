class PriorityQueue:
    """
    Min-priority queue implemented using a binary heap.

    Each item is stored as:
        (priority, value)

    Lower priority value means higher priority.
    """

    def __init__(self):
        self.heap = []

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self.heap) == 0

    def push(self, priority, value):
        """Insert an item into the priority queue."""
        self.heap.append((priority, value))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """
        Remove and return the item with the smallest priority.

        Returns:
            tuple: (priority, value)

        Raises:
            IndexError: if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty priority queue.")

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return minimum

    def peek(self):
        """Return the highest-priority item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty priority queue.")

        return self.heap[0]

    def _heapify_up(self, index):
        """Restore heap property upward."""

        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index][0] >= self.heap[parent][0]:
                break

            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index],
            )

            index = parent

    def _heapify_down(self, index):
        """Restore heap property downward."""

        size = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            smallest = index

            if (
                left < size
                and self.heap[left][0] < self.heap[smallest][0]
            ):
                smallest = left

            if (
                right < size
                and self.heap[right][0] < self.heap[smallest][0]
            ):
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )

            index = smallest