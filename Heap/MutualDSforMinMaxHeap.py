class Node:
    def __init__(self, data):
        self.data = data
        self.min_index = 0
        self.max_index = 0
        self.next = self.prev = None

    def delete_node(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next
        del self


class Heap:
    def __init__(self):
        self.root = None
        self.min_heap = []
        self.max_heap = []

    @staticmethod
    def get_parent(i):
        return (i - 1) // 2

    @staticmethod
    def get_child(i, pos):
        return (i * 2) + pos

    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def insert_data(self, data):
        node = Node(data)
        if self.root:
            self.root.prev = node
            node.next = self.root
        self.root = node
        self.insert_min_heap()
        self.insert_max_heap()

    def min_heapify(self, i):
        n = len(self.min_heap)
        root = i
        l = Heap.get_child(i, 1)
        r = Heap.get_child(i, 2)
        if l < n and self.min_heap[l].data < self.min_heap[root].data:
            root = l
        if r < n and self.min_heap[l].data < self.min_heap[root].data:
            root = r
        if root != i:
            self.min_heap[root].min_index, self.min_heap[i].min_index = i, root
            Heap.swap(self.min_heap, root, i)
            self.min_heapify(root)

    def max_heapify(self, i):
        n = len(self.max_heap)
        root = i
        l = Heap.get_child(i, 1)
        r = Heap.get_child(i, 2)
        if l < n and self.max_heap[l].data > self.max_heap[root].data:
            root = l
        if r < n and self.max_heap[r].data > self.max_heap[root].data:
            root = r
        if root != i:
            self.max_heap[root].max_index, self.max_heap[i].max_index = i, root
            Heap.swap(self.max_heap, root, i)
            self.max_heapify(root)

    def insert_min_heap(self):
        self.min_heap.append(self.root)
        i = len(self.min_heap) - 1
        self.root.min_index = i
        while i > 0:
            p = Heap.get_parent(i)
            if self.min_heap[i].data < self.min_heap[p].data:
                self.min_heap[i].min_index, self.min_heap[p].min_index = p, i
                Heap.swap(self.min_heap, i, p)
            else:
                return
            i = p

    def insert_max_heap(self):
        self.max_heap.append(self.root)
        i = len(self.max_heap) - 1
        self.root.max_index = i
        while i > 0:
            p = Heap.get_parent(i)
            if self.max_heap[i].data > self.max_heap[p].data:
                self.max_heap[i].max_index, self.max_heap[p].max_index = p, i
                Heap.swap(self.max_heap, i, p)
            else:
                return
            i = p

    def get_min(self):
        if self.min_heap:
            return self.min_heap[0].data

    def get_max(self):
        if self.max_heap:
            return self.max_heap[0].data

    def extract_min(self):
        node = self.min_heap[0]
        self.min_heap[0] = self.min_heap[-1]
        self.min_heap[0].min_index = 0
        del self.min_heap[-1]
        self.min_heapify(0)


        self.max_heap[node.max_index] = self.max_heap[-1]
        self.max_heap[node.max_index].max_index = node.max_index
        del self.max_heap[-1]
        self.max_heapify(node.max_index)

        node.delete_node()

    def extract_max(self):
        node = self.max_heap[0]
        self.max_heap[0] = self.max_heap[-1]
        self.max_heap[0].max_index = 0
        del self.max_heap[-1]
        self.max_heapify(0)

        self.min_heap[node.min_index] = self.min_heap[-1]
        self.min_heap[node.min_index].min_index = node.min_index
        del self.min_heap[-1]
        self.min_heapify(node.min_index)

        node.delete_node()

    def delete_data(self, data):
        itr = self.root
        node = None
        while itr and not node:
            if itr.data == data:
                node = itr
            itr = itr.next
        if not node:
            return

        self.min_heap[node.min_index] = self.min_heap[-1]
        self.min_heap[node.min_index].min_index = node.min_index
        del self.min_heap[-1]
        self.min_heapify(node.min_index)

        self.max_heap[node.max_index] = self.max_heap[-1]
        self.max_heap[node.max_index].max_index = node.max_index
        del self.max_heap[-1]
        self.max_heapify(node.max_index)

        node.delete_node()


if __name__ == "__main__":
    heap = Heap()
    heap.insert_data(10)
    heap.insert_data(8)
    heap.insert_data(15)
    heap.insert_data(25)
    heap.insert_data(18)
    heap.insert_data(35)
    heap.delete_data(25)

    print(heap.get_max())
    print(heap.get_min())
    for i in range(len(heap.min_heap)):
        print("{0},{1}".format(heap.min_heap[i].data, heap.max_heap[i].data))

