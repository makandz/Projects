from typing import List

"""
Heap that can store integers.
"""
class Heap:
    _heap: List[int]
    _size: int

    def __init__(self) -> None:
        self._heap = [-1] # first index not used
        self._size = 0

    def __str__(self) -> str:
        return str(self._heap)

    def _MaxHeapify(self, i: int) -> None:
        """
        Bubble down to restore heap properties starting from index <i>.
        Runtime: O(logn) [height of tree]
        ~Code Provided: W2 Lecture
        """
        left = 2 * i
        right = (2 * i) + 1
        if left <= self._size and self._heap[left] > self._heap[i]:
            largest = left
        else:
            largest = i
        if right <= self._size and self._heap[right] > self._heap[largest]:
            largest = right
        if largest != i:
            self._heap[largest], self._heap[i] = \
                self._heap[i], self._heap[largest]
            self._MaxHeapify(largest)

    def Create(self, heap: List[int]) -> None:
        """
        Creates a new heap from <heap> list.
        Runtime: O(n logn) [size * height of tree]
        """
        self._heap = [-1] + heap
        self._size = len(heap)
        for i in range(self._size, 0, -1):
            self._MaxHeapify(i)

    def Sort(self) -> List[int]:
        """
        Sort the heap in place and return the sorted heap. This will destroy 
        the heap!
        Runtime: O(n logn) [size * height of tree]
        """
        while self._size > 0:
            self._heap[self._size], self._heap[1] = \
                self._heap[1], self._heap[self._size]
            self._size -= 1
            self._MaxHeapify(1)
        
        heap = self._heap[1:]
        self.__init__() # reset
        return heap

    def Insert(self, x: int) -> None:
        """
        Insert <x> with priority of it's value into queue.
        Runtime: O(1)
        """
        self._heap.append(x)
        self._size += 1
        i = self._size # end of list

        while i > 1: # bubble up
            parent_index = i // 2 # floor down
            if self._heap[i] > self._heap[parent_index]:
                # swap parent and child
                self._heap[i], self._heap[parent_index] = \
                    self._heap[parent_index], self._heap[i]
            else:
                break
            i = parent_index

    def FindMax(self) -> int:
        """
        Find the value with the max priority.
        Runtime: O(1)
        """
        return self._heap[1]

    def ExtractMax(self) -> int:
        """
        Extract the value with the max priority from the queue.
        Runtime: O(logn) [height of tree]
        """
        # swap parent with child
        self._heap[1], self._heap[self._size] = \
            self._heap[self._size], self._heap[1]
        
        self._size -= 1 # reduce size
        largest = self._heap.pop() # remove child (now the largest)
        self._MaxHeapify(1) # restore properties -> O(logn)
        return largest

if __name__ == "__main__":
    heap = Heap()
    heap.Insert(2)
    print(heap)
    heap.Insert(17)
    heap.Insert(5)
    heap.Insert(13)
    print(heap)
    print(heap.ExtractMax())
    print(heap.ExtractMax())
    print(heap.ExtractMax())
    print(heap.ExtractMax())
    print(heap)

    print()

    heap = Heap()
    heap.Create([2, 5, 1, 23, 10, 92, 10, 100, 219, 100])
    print(heap.ExtractMax())
    print(heap.ExtractMax())
    print(heap.ExtractMax())
    print(heap)
    print(heap.Sort())
    print(heap)
