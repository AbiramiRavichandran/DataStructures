# Import the heap functions from python library
#from heapq import heappush, heappop, heapify

class MinHeap:

    def __init__(self):
        self.heap = []

    #equivalent to heapify
    def heapify_imp(self, i):
        while i != 0 and self.heap[MinHeap.parent(i)] > self.heap[i]:
            parent = MinHeap.parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    @classmethod
    def parent(cls, i):
        return (i - 1) // 2

    #heappush(self.heap, k) - equivalent to library function
    def insert_key(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        self.heapify_imp(i)


    #equivalent to heappop
    def extract_min(self):
        min = self.heap[0]
        del self.heap[0]
        self.heapify_imp(len(self.heap) - 1)
        return min

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        self.heapify_imp(i)



    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()


    def get_min(self):
        return self.heap[0]


if __name__ == "__main__":
    heapObj = MinHeap()
    heapObj.insert_key(3)
    heapObj.insert_key(2)
    heapObj.delete_key(1)
    heapObj.insert_key(15)
    heapObj.insert_key(5)
    heapObj.insert_key(4)
    heapObj.insert_key(45)

    print(heapObj.heap)

    print(heapObj.extract_min())
    print(heapObj.get_min())
    heapObj.decrease_key(2, 1)
    print(heapObj.get_min())
